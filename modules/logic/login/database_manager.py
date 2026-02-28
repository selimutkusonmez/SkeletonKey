import psycopg2
import datetime

class DatabaseManager:
    def __init__(self):
        self.conn_params = {
            "host": "127.0.0.1",
            "port": "5432",
            "database": "skeleton_db",
            "user": "admin",
            "password": "1234"
        }
        self.connect_db()

    def connect_db(self):
        self.conn = psycopg2.connect(**self.conn_params)
        self.cursor = self.conn.cursor()

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