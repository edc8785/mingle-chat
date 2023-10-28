from database import *
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/post", methods=["POST"])
def post():
    # 클라이언트에서 Firebase 토큰을 추출
    firebase_token = request.headers.get("Authorization").split(" ")[1]

    # Firebase 토큰 검증
    result = verify_firebase_token(firebase_token)
    if isinstance(result, dict):
        # Firebase 토큰 검증 성공
        username = result["name"]  # 사용자 이름은 Firebase 토큰에서 추출
        content = request.json.get("content")
        if username and content:
            # 사용자 글 저장
            save_user_post(username, content)
            return jsonify({"message": "게시물 저장 성공"})
        else:
            return jsonify({"message": "게시물 저장 실패"})
    else:
        return jsonify({"message": "Firebase 토큰 검증 실패"})




if __name__ == "__main__":
    app.run()

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

    # Firebase 토큰
    firebase_token = "YOUR_FIREBASE_TOKEN_HERE"
    # 토큰 검증
    result = user_manager.verify_firebase_token(firebase_token)
    if isinstance(result, dict):
        print("Firebase 토큰 검증 성공")
        print("UID:", result["uid"])
        print("클레임:", result)
    else:
        print("Firebase 토큰 검증 실패:", result)

    # 사용자 등록
    user_manager.register_user("testuser", "testpassword")

    # 사용자 로그인
    login_result = user_manager.login("testuser", "testpassword")
    if login_result:
        print("사용자 로그인 성공")
    else:
        print("사용자 로그인 실패")

    # 사용자 글 저장
    user_manager.save_user_post("testuser", "사용자가 작성한 글입니다.")
    print("사용자 글 저장 완료")