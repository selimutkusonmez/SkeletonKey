import psycopg2

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
            else : 
                return 0
            
        except Exception as e:
            print(f"DB Error: {e}")
            return False
        
    def make_history(self,username,mode,algorithm,key,input_text,output_text):
        print(username)
        print(mode)
        print(algorithm)
        print(key)
        print(input_text)
        print(output_text)
        try:
            query = """
                    INSERT INTO history (user_id,mode,algorithm,key,input_text,output_text)
                    VALUES (
                            (SELECT id FROM users WHERE username = %s), %s, %s, %s, %s, %s
                        ) RETURNING id;
                    """
            self.cursor.execute(query,(username,mode,algorithm,key,input_text,output_text))

            self.conn.commit()
            db_id = self.cursor.fetchone()
            print(db_id)

            if db_id:
                print(f"Başarıyla kaydedildi. ID: {db_id}")
                return db_id
            else:
                print("Hata: Veritabanından ID dönmedi! Kullanıcı adı doğru mu?")
                return None
        except Exception as e:
            self.conn.rollback()
            print(f"History Error: {e}")
            return None

        
    def __del__(self):
        if hasattr(self, 'conn') and self.conn is not None:
            self.conn.close()