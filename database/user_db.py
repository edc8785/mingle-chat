import pymysql
from database.user_table import UserTable

class UserDB:
    def __init__(self):
        f = open('aws_token.txt', 'r') 
        lines = f.readlines()
        f.close()

        self.host = lines[0].replace("\n", "")
        self.port = lines[1].replace("\n", "")
        self.user = lines[2].replace("\n", "")
        self.db = lines[3].replace("\n", "")
        self.password = lines[4].replace("\n", "")
        self.conn = None
        
    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8')

    def disconn(self):
        self.conn.close()

    def create_table(self, sql):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.disconn()
    
    def show_tables(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute('SHOW TABLES;')
        result = cursor.fetchall()
        self.disconn()
        return result

    def insert(self, user:UserTable):
        self.connect()
        cursor = self.conn.cursor()

        sql = 'insert into user_db(id, pwd, name, message, description) values(%s, %s, %s, %s, %s)'
        raw = (user.id, user.pwd, user.name, user.message, user.description)

        cursor.execute(sql, raw)
        self.conn.commit()
        self.disconn()

    def select(self, id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'select * from user_db where id=%s'
            d = (id, )
            cursor.execute(sql, d)
            row = cursor.fetchone()
            if row:
                return UserTable(row[0], row[1], row[2], row[3], row[4])
        
        except Exception as e:
            print(e)
        finally:
            self.disconn()


    def selectAll(self):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'select * from user_db'
            cursor.execute(sql)
            res = [UserTable(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
            return res
        
        except Exception as e:
            print(e)

        finally:
            self.disconn()