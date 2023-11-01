from database import *

f = open('aws_token.txt', 'r') 
lines = f.readlines()
f.close()

db_host = lines[0].replace("\n", "")
db_port = lines[1].replace("\n", "")
db_user = lines[2].replace("\n", "")
db_database = lines[3].replace("\n", "")
db_password = lines[4].replace("\n", "")
service_account_key_path = "mingle-chat-fb-firebase-adminsdk-pb2jz-3db7100a19.json"

user_manager = firebase.UserManagement(db_host, db_user, db_password, db_database, service_account_key_path)
user_manager.register_user("test_email","test_password","test","test","test","test")
user_manager.delete_user("test_email")
user_manager.login_user("test_email","test_password")

user_manager.save_user_post("test_email", "test_title", "title_main")
user_manager.save_user_post("test_email", "test_title2", "title_main2")
user_manager.save_user_post("test_email", "test_title3", "title_main3")
user_manager.save_user_post("test_email", "test_title4", "title_main4")


import mysql.connector
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

my_connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )



cursor = my_connection.cursor()
select_user_id_query = "SELECT user_id FROM users WHERE email = %s"
cursor.execute(select_user_id_query, ("test_email",))
user_id = cursor.fetchone()
insert_post_query = "INSERT INTO user_posts (user_id, email, content_title, content_main) VALUES (%s, %s, %s, %s)"
cursor.execute(insert_post_query, (user_id[0], "test_email",  "test_title", "title_main"))
my_connection.commit()

select_post_id_query = "SELECT post_id FROM user_posts WHERE email = %s ORDER BY created_at DESC"
cursor.execute(select_post_id_query, ("test_email",))
post_id = cursor.fetchone()
post_id = cursor.fetchone()


"""
from database import *
service_account_key_path = "mingle-chat-fb-firebase-adminsdk-pb2jz-3db7100a19.json"

import mysql.connector
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
# Firebase Admin SDK 초기화
cred = credentials.Certificate(service_account_key_path)
firebase_admin.initialize_app(cred)

user = auth.get_user_by_email("edc8786@g.skku.edu")
user.uid



current_user = auth.get_user(uid=user.uid)
current_user = auth.get_user("CzEbalGFi4YPM9t2Hp6Jl7ASmEq1")
current_user = auth.get_user("test")
current_user.display_name

auth.verify_id_token(user.uid)

import requests

# Firebase Cloud Function 또는 엔드포인트 URL (실제 Firebase 프로젝트에 맞게 수정)
firebase_url = "https://your-firebase-app-url.com/your-function-endpoint"
# 사용자의 ID 토큰
user_id_token = "사용자의_ID_토큰_입력"
# 요청 헤더에 ID 토큰 추가
headers = {
    "Authorization": f"Bearer {user_id_token}"
}

# POST 요청 예시 (원하는 방식 선택)
response = requests.post(firebase_url, headers=headers, data={"key": "value"})

# 응답 출력
print(response.status_code)
print(response.text)
"""