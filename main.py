from database import *
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'mingle-chat'
    
# 회원가입 API
@app.route('/create_user', methods=['POST'])
def create_user_api():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user_id = firebase.register_user(email, password)
    return jsonify({"message": "User created successfully", "user_id": user_id})

# 로그인 API
@app.route('/login', methods=['POST'])
def login_api():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user_id = firebase.login_user(email, password)
    if isinstance(user_id, str):
        return jsonify({"error": user_id}), 401
    return jsonify({"message": "Login successful", "user_id": user_id})

# 회원탈퇴 API
@app.route('/delete_user', methods=['POST'])
def delete_user_api():
    data = request.get_json()
    user_id = data['user_id']
    result = firebase.delete_user(user_id)
    if isinstance(result, str):
        return jsonify({"error": result}), 400
    return jsonify({"message": result})


# 게시글 조회
@app.route("/get_post", methods=["GET"])
def get_posts():
    username = request.args.get("username")
    if username:
        # 사용자 게시글 조회
        posts = firebase.get_user_posts(username)
        return jsonify({"posts": posts})
    else:
        return jsonify({"message": "게시글 조회 실패"})

# 게시글 삭제
@app.route("/delete_post", methods=["POST"])
def delete_post():
    username = request.json.get("username")
    post_id = request.json.get("post_id")
    if username and post_id:
        # 사용자 게시글 삭제
        firebase.delete_user_post(username, post_id)
        return jsonify({"message": "게시글 삭제 성공"})
    else:
        return jsonify({"message": "게시글 삭제 실패"})

# 게시글 작성
@app.route("/create_post", methods=["POST"])
def create_post():
    # 클라이언트에서 Firebase 토큰을 추출
    firebase_token = request.headers.get("Authorization").split(" ")[1]

    # Firebase 토큰 검증
    result = firebase.verify_firebase_token(firebase_token)
    if isinstance(result, dict):
        # Firebase 토큰 검증 성공
        username = result["name"]  # 사용자 이름은 Firebase 토큰에서 추출
        content = request.json.get("content")
        if username and content:
            # 사용자 글 저장
            firebase.save_user_post(username, content)
            return jsonify({"message": "게시물 저장 성공"})
        else:
            return jsonify({"message": "게시물 저장 실패"})
    else:
        return jsonify({"message": "Firebase 토큰 검증 실패"})



## flask hosting
if __name__ == "__main__":
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
    app.run()



"""
test code

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

user_manager.login("test_email","test_password")
user_manager.save_user_post("test_email", "test_title", "title_main")
user_manager.get_user_post("test_email")
user_manager.delete_user_post("test_email",1)
"""