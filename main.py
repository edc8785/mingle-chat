from database import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'mingle-chat'

@app.route('/postman', methods=['GET','POST'])
def postman():
    if(request.method == 'GET'):
        return "GET-test"
    elif(request.method == 'POST'):
        return "POST-test"
    else:
        return "Not allowed method"



# 회원가입 API
@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data['email']
    password = data['password']
    profile_img_url = data['profile_img_url']
    activity_name = data['activity_name']
    message = data['message']
    description = data['description']
    interest_category = data['interest_category']
    sns_url = data['sns_url']

    user_id = user_manager.register_user(email, password, profile_img_url, activity_name, message, description, interest_category, sns_url)
    if user_id:
        return jsonify({"message": "User created successfully", "user_id": user_id}), 200
    else:
        return jsonify({"error": "Failed to register user"}), 500


# 회원탈퇴 API
@app.route('/delete_user', methods=['POST'])
def delete_user():
    data = request.get_json()
    user_id = data['user_id']

    if user_id:
        result = user_manager.delete_user(user_id)
        if result:
            return jsonify({"message": "delete successful"}), 200
        else:
            return jsonify({"error": "Failed to delete user"}), 500
    else:
        return jsonify({"error": "Missing 'user_id' in the request"}), 400



# 특정 ID의 게시글 조회 (GET 요청)
@app.route('/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def get_post():
    if(request.method == 'GET'):
        data = request.get_json()
        post_id = data["post_id"]

        post = user_manager.get_user_post()
        return jsonify({"posts":post}), 200

        ##return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

    elif(request.method == 'PUT'):
        data = request.get_json()
        post_id = data["post_id"]

        post = user_manager.get_user_post()
        return jsonify({"posts":post}), 200

        ##return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

    elif(request.method == 'DELETE'):
        data = request.get_json()
        post_id = data["post_id"]

        post = user_manager.get_user_post()
        return jsonify({"posts":post}), 200

        ##return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404


    else:
        return jsonify({"error": "허용되지 않는 요청입니다."}), 405


# 모든 게시글 조회 (GET 요청)
@app.route('/posts', methods=['GET', 'POST'])
def get_posts():
    if(request.method == 'GET'):
        data = request.get_json()
        post_id = data["post_id"]

        post = user_manager.get_user_post()
        return jsonify({"posts":post}), 200
        ## return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

    elif request.method == 'POST':
        data = request.get_json()
        post_id = data["post_id"]

        post = user_manager.get_user_post()
        return jsonify({"posts":post}), 200
        ## return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

    else:
        return jsonify({"error": "허용되지 않는 요청입니다."}), 405






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
