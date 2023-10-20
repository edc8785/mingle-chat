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

    def create_table(self):
        self.connect()
        cursor = self.conn.cursor()
        self.disconn()
    
    def show_tables(self):
        self.connect()
        cursor = self.conn.cursor()
        result = cursor.execute('SHOW TABLES')
        self.disconn()
        return result

    def insert(self, user:UserTable):
        self.connect()
        cursor = self.conn.cursor()

        sql = 'insert into member(id, pwd, name, email) values(%s, %s, %s, %s)'
        raw = (user.id, user.pwd, user.name, user.email)

        cursor.execute(sql, raw)
        self.conn.commit()
        self.disconn()


