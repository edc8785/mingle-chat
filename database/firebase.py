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
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)

    # 토큰 검증 함수
    def verify_firebase_token(self, id_token):
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except auth.ExpiredIdTokenError:
            return "Token has expired"
        except auth.InvalidIdTokenError:
            return "Invalid token"

    # 사용자 등록
    def register_user(self, username, password):
        with self.connection.cursor() as cursor:
            insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(insert_user_query, (username, password))
        self.connection.commit()

    # 사용자 탈퇴 (추가)
    def delete_user(self, username):
        with self.connection.cursor() as cursor:
            delete_user_query = "DELETE FROM users WHERE username = %s"
            cursor.execute(delete_user_query, (username,))
        self.connection.commit()

    # 사용자 로그인
    def login(self, username, password):
        with self.connection.cursor() as cursor:
            select_user_query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(select_user_query, (username,))
            user = cursor.fetchone()
            if user and user[2] == password:
                return True
            return False

    # 사용자 글 저장
    def save_user_post(self, username, content):
        with self.connection.cursor() as cursor:
            select_user_id_query = "SELECT id FROM users WHERE username = %s"
            cursor.execute(select_user_id_query, (username,))
            user_id = cursor.fetchone()
            if user_id:
                insert_post_query = "INSERT INTO posts (user_id, content) VALUES (%s, %s)"
                cursor.execute(insert_post_query, (user_id[0], content))
                self.connection.commit()

    # 사용자 게시글 조회 (추가)
    def get_user_posts(self, username):
        with self.connection.cursor() as cursor:
            select_posts_query = "SELECT content FROM posts WHERE user_id = (SELECT id FROM users WHERE username = %s)"
            cursor.execute(select_posts_query, (username,))
            posts = cursor.fetchall()
            return [post[0] for post in posts]

    # 사용자 게시글 삭제 (추가)
    def delete_user_post(self, username, post_id):
        with self.connection.cursor() as cursor:
            delete_post_query = "DELETE FROM posts WHERE user_id = (SELECT id FROM users WHERE username = %s) AND id = %s"
            cursor.execute(delete_post_query, (username, post_id))
        self.connection.commit()


