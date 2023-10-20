from database import *

if __name__ == '__main__':
    print(__name__)
    db = user_db.UserDB()
    print(db.show_tables())
    all_user = db.selectAll()
    print(all_user)


db = user_db.UserDB()
db.connect()
cursor = db.conn.cursor()

cursor.execute("""
               CREATE TABLE user_db(
               id VARCHAR(255) not null,
               pwd VARCHAR(255) not null,
               name VARCHAR(255) not null,
               message VARCHAR(255),
               description VARCHAR(255));
               """)

db.show_tables()

db.insert(user_table.UserTable("sample_id_1","sample_pwd_1","sample_name_1","나만의 길을 찾을 때까지 인생이라는 게임의 레버를 당기는 법","좋아하는 일로 행복하게 일하는 상위 1% 밀레니얼 프리워커 드로우앤드류입니다."))
cursor.execute("select * from user_db")
cursor.fetchall()
cursor.execute('DROP TABLE user_db')
cursor.execute('delete from user_db where id="sample_id_1"')