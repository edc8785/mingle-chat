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
    def register_user(self, email, password, profile_img_url, activity_name, message, description, interest_category, sns_url):
        try:
            ## insert user table
            cursor = self.connection.cursor()
            insert_user_query = "INSERT INTO users (email, password, profile_img_url, activity_name, message, description, interest_category, sns_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_user_query, (email, password, profile_img_url, activity_name, message, description, interest_category, sns_url))
            self.connection.commit()

            ## return mysql user_id 
            select_user_id_query = "SELECT user_id FROM users WHERE email = %s"
            cursor.execute(select_user_id_query, (email,))
            (user_id,) = cursor.fetchone()
            cursor.close()
            return user_id
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return None
        
        
    # 사용자 탈퇴
    def delete_user(self, user_id):
        try:
            cursor = self.connection.cursor()
            delete_user_query = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(delete_user_query, (user_id,))
            self.connection.commit()
            cursor.close()
            return True
        
        except Exception as e:
            print(f"Error: {str(e)}")
            return False  # 예외 발생 시 False 반환
        
        
    # 사용자 글 저장
    def save_post(self, user_id, project_name, category, period, intro, offer):
        try:
            ## insert post table
            cursor = self.connection.cursor()       
            insert_post_query = "INSERT INTO posts (user_id, project_name, category, period, intro, offer) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_post_query, (user_id, project_name, category, period, intro, offer))
            self.connection.commit()

            ## return mysql post_id
            select_post_id_query = "SELECT post_id FROM posts WHERE user_id = %s ORDER BY created_at DESC LIMIT 1"
            cursor.execute(select_post_id_query, (user_id,))
            (post_id,) = cursor.fetchone()
            cursor.close()
            return post_id

        except Exception as e:
            print(f"Error: {str(e)}")
            return None
        

    # 전체 게시글 조회 (all)
    def get_post_all(self):
        try:
            cursor = self.connection.cursor()
            select_post_query = "SELECT * FROM posts"
            cursor.execute(select_post_query)
            posts = cursor.fetchall()
            cursor.close()
            return [post for post in posts]
        except Exception as e:
            print(f"Error: {str(e)}")
            return None
            
            
    # 사용자별 게시글 조회 (one)
    def get_post_user(self, user_id):
        try:
            cursor = self.connection.cursor()
            select_post_query = "SELECT * FROM posts WHERE user_id = %s"
            cursor.execute(select_post_query, (user_id,))
            posts = cursor.fetchall()
            cursor.close()
            return [post for post in posts]
        except Exception as e:
            print(f"Error: {str(e)}")
            return None       



    # 사용자 게시글 삭제 (추가)
    def delete_post(self, post_id):
        try:
            cursor = self.connection.cursor()
            delete_post_query = "DELETE FROM posts WHERE post_id = %s"
            cursor.execute(delete_post_query, (post_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error: {str(e)}")
            return False  # 예외 발생 시 False 반환

