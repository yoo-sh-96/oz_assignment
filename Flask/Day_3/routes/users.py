from flask import request, jsonify  # 요청 수신 및 응답 반환
from flask.views import MethodView  # 클래스 기반 뷰를 위한 모듈
from flask_smorest import Blueprint  # API 라우팅 모듈화
from db import db  # DB 세션
from models import User  # 사용자 모델

# 사용자 관련 API를 위한 블루프린트 정의
user_blp = Blueprint('Users', 'users', description='Operations on users', url_prefix='/users')

# /users/ 경로에서 전체 사용자 조회 및 새 사용자 등록 처리
@user_blp.route('/')
class UserList(MethodView):
    def get(self):  # 사용자 전체 목록 반환
        users = User.query.all()  # DB에서 전체 사용자 가져오기
        user_data = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
        return jsonify(user_data)  # JSON 응답 반환

    def post(self):  # 사용자 등록 처리
        print("요청은 오는가?")  # 로그 출력
        user_data = request.json  # JSON 형태로 요청 데이터 받기
        new_user = User(name=user_data['name'], email=user_data['email'])  # 새 User 인스턴스 생성
        db.session.add(new_user)  # DB에 추가
        db.session.commit()  # 저장
        return jsonify({"message": "User created"}), 201  # 성공 응답

# /users/<user_id> 경로에서 특정 사용자 조회, 수정, 삭제
@user_blp.route('/<int:user_id>')
class Users(MethodView):
    def get(self, user_id):  # 특정 사용자 정보 반환
        user = User.query.get_or_404(user_id)
        return {"name": user.name, 'email': user.email}

    def put(self, user_id):  # 사용자 정보 수정
        user = User.query.get_or_404(user_id)
        user_data = request.json
        user.name = user_data['name']  # 이름 수정
        user.email = user_data['email']  # 이메일 수정
        db.session.commit()
        return {"message": "User updated"}

    def delete(self, user_id):  # 사용자 삭제
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}