import mysql.connector
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class UserManagement:
    def __init__(self, db_host, db_user, db_password, db_database, service_account_key_path):
        # AWS RDS 연결 설정
        self.connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        # Firebase Admin SDK 초기화
        ## cred = credentials.Certificate(service_account_key_path)
        ## firebase_admin.initialize_app(cred)

    # 토큰 검증 함수
    def verify_firebase_token(self, id_token):
        """
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except auth.ExpiredIdTokenError:
            return "Token has expired"
        except auth.InvalidIdTokenError:
            return "Invalid token"
        """
        return True
        
    # 사용자 등록
    def register_user(self, email, password, activity_name, message, description, interest_category):
        cursor = self.connection.cursor()
        insert_user_query = "INSERT INTO users (email, password, activity_name, message, description, interest_category) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_user_query, (email, password, activity_name, message, description, interest_category))
        self.connection.commit()

    # 사용자 탈퇴 (추가)
    def delete_user(self, email):
        cursor = self.connection.cursor()
        delete_user_query = "DELETE FROM users WHERE email = %s"
        cursor.execute(delete_user_query, (email,))
        self.connection.commit()

    # 사용자 로그인
    def login(self, email, password):
        cursor = self.connection.cursor()
        select_user_query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(select_user_query, (email,))
        user = cursor.fetchone()
        if user and user[2] == password:
            return True
        return False
    
    # 사용자 글 저장
    def save_user_post(self, email, content_title, content_main):
        cursor = self.connection.cursor()
        select_user_id_query = "SELECT user_id FROM users WHERE email = %s"
        cursor.execute(select_user_id_query, (email,))
        user_id = cursor.fetchone()
        if user_id:
            insert_post_query = "INSERT INTO user_posts (user_id, email, content_title, content_main) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_post_query, (user_id[0], email, content_title, content_main))
            self.connection.commit()

    # 사용자 게시글 조회 (추가)
    def get_user_post(self, email):
        cursor = self.connection.cursor()
        select_post_query = "SELECT content_title, content_main FROM user_posts WHERE user_id = (SELECT user_id FROM users WHERE email = %s)"
        cursor.execute(select_post_query, (email,))
        posts = cursor.fetchall()
        return [[post[0], post[1]] for post in posts]


    # 사용자 게시글 삭제 (추가)
    def delete_user_post(self, email, post_id):
        cursor = self.connection.cursor()
        delete_post_query = "DELETE FROM user_posts WHERE user_id = (SELECT user_id FROM users WHERE email = %s) AND post_id = %s"
        cursor.execute(delete_post_query, (email, post_id))
        self.connection.commit()


