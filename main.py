from database import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'mingle-chat'

@app.route('/postman', methods=['GET','POST'])
def postman():
    return "post-test"

@app.route('/add_two_nums', methods=['POST'])
def add() :
    # 클라이언트로부터 두 수를 받는다. request 라이브러리 사용
    data = request.get_json()
    ret = data['x'] + data['y']
    result = {'result' : ret}
    return jsonify(result)


# 회원가입 API
@app.route('/register_user_api', methods=['POST'])
def register_user_api():
    data = request.get_json()
    email = data['email']
    password = data['password']
    activity_name = data['activity_name']
    message = data['message']
    description = data['description']
    interest_category = data['interest_category']

    user_id = user_manager.register_user(email, password, activity_name, message, description, interest_category)
    return jsonify({"message": "User created successfully", "user_id": user_id})


# 로그인 API
@app.route('/login_user_api', methods=['POST'])
def login_user_api():
    data = request.get_json()
    email = data['email']
    password = data['password']
    if user_manager.login_user(email, password):
        return jsonify({"message": "Login successful"})
    return jsonify({"error"}), 401


# 회원탈퇴 API
@app.route('/delete_user_api', methods=['POST'])
def delete_user_api():
    data = request.get_json()
    email = data['email']
    user_manager.delete_user(email)


# 게시글 조회
@app.route("/get_post_api", methods=["GET"])
def get_post_api():
    data = request.get_json()
    email = data['email']
    if email:
        # 사용자 게시글 조회
        posts = user_manager.get_user_post(email)
        return jsonify({"posts": posts})
    else:
        return jsonify({"message": "게시글 조회 실패"})

# 게시글 삭제
@app.route("/delete_post_api", methods=["POST"])
def delete_post_api():
    data = request.get_json()
    email = data["email"]
    post_id = data["post_id"]
    if email and post_id:
        # 사용자 게시글 삭제
        user_manager.delete_user_post(email, post_id)
        return jsonify({"message": "게시글 삭제 성공"})
    else:
        return jsonify({"message": "게시글 삭제 실패"})

# 게시글 작성
@app.route("/save_post_api", methods=["POST"])
def save_post_api():
    # 클라이언트에서 Firebase 토큰을 추출
    ##firebase_token = request.headers.get("Authorization").split(" ")[1]
    # Firebase 토큰 검증
    ##result = firebase.verify_firebase_token(firebase_token)
    data = request.get_json()
    email = data["email"]
    content_title = request.json.get("content_title")
    content_main = request.json.get("content_main")
    
    if email and content_title and content_main:
        post_id = user_manager.save_user_post(email, content_title, content_main)
        return jsonify({"message": "게시물 저장 성공", "post_id":post_id})
    else:
        return jsonify({"message": "게시물 저장 실패"})




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
    app.run(host="0.0.0.0", port="5000")



