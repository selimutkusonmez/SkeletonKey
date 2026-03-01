import psycopg2
import datetime
import subprocess
import time

class DatabaseManager:
    def __init__(self):
        self.conn_params = {
            "host": "127.0.0.1",
            "port": "5432",
            "database": "skeleton_db",
            "user": "admin",
            "password": "1234",
            "connect_timeout": 2
        }
        self.start_docker_and_connect_db()

    def start_docker_and_connect_db(self):
        print("Checking system status...")
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            self.cursor = self.conn.cursor()
            print("✅ Database is already running! Skipping Docker command.")
            return True
        except psycopg2.OperationalError:
            print("⚠️ Database is down. Starting Docker...")

        try:
            subprocess.run(["docker-compose","up","-d"],check=True)
        except Exception as e:
            print(f"❌ Critical Error: Failed to execute Docker command! Error: {e}")
            return False

        max = 10
        for i in range(max):
            try:
                self.conn = psycopg2.connect(**self.conn_params)
                self.cursor = self.conn.cursor()
                print("✅ Docker and Database successfully started and ready!")
                return True
            except psycopg2.OperationalError:
                print(f"⏳ Waiting for database to wake up... ({i+1}/{max})")
                time.sleep(1)


    def check_login(self, username, password):
        try:
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            user = self.cursor.fetchone()            
            if user:
                return 1    
            else: 
                return 0
                
        except Exception as e:
            self.conn.rollback()
            return f"Error: {str(e)}"
        
    def make_history(self, username, mode, algorithm, key, input_text, output_text):
        try:
            query = """
                    INSERT INTO history (user_id,date,mode,algorithm,key,input_text,output_text)
                    VALUES (
                            (SELECT id FROM users WHERE username = %s), %s, %s, %s, %s, %s, %s
                        ) RETURNING id;
                    """
            
            self.cursor.execute(query, (username, datetime.datetime.now(), mode, algorithm, key, input_text, output_text))

            self.conn.commit()
            db_id = self.cursor.fetchone()

            if db_id:
                return db_id[0]
            else:
                return None
                
        except Exception as e:
            self.conn.rollback()
            return f"Error: {str(e)}"

    def show_clicked_history(self, db_id):
        try:
            query = "SELECT * FROM history WHERE id = %s"
            self.cursor.execute(query, (db_id,))
            data = self.cursor.fetchone()
            return data
            
        except Exception as e:
            self.conn.rollback()
            return f"Error: {str(e)}"
        
    def show_history_by_date(self, username, start_date, end_date):
        try:
            query = "SELECT * FROM history WHERE user_id = (SELECT id FROM users WHERE username = %s) AND date::date BETWEEN %s AND %s ORDER BY date DESC"
            self.cursor.execute(query, (username, start_date, end_date))
            data = self.cursor.fetchall()
            return data
            
        except Exception as e:
            self.conn.rollback()
            return f"Error: {str(e)}"
        
    def __del__(self):
        if hasattr(self, 'conn') and self.conn is not None:
            self.conn.close()