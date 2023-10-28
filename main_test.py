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
