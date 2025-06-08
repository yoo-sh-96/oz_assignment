from flask import Flask  # Flask 웹 서버를 만들기 위한 클래스
from flask_smorest import Api  # Swagger 문서 자동 생성 기능 포함된 API 시스템
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy: ORM 사용 위한 라이브러리
from db import db  # db.py에서 만든 SQLAlchemy 인스턴스 불러오기
from models import User, Board  # DB 모델 클래스 불러오기

app = Flask(__name__)  # Flask 웹 앱 생성

# MySQL DB 연결 정보 입력
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1q2w3e4r@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # SQLAlchemy 내부 변경사항 추적 안함

db.init_app(app)  # Flask 앱에 DB 연결 적용

# OpenAPI + Swagger UI 설정 (API 문서 자동 생성용)
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# 블루프린트 등록 (API 기능을 분리해서 관리)
from routes.users import user_blp
from routes.board import board_blp

api = Api(app)
api.register_blueprint(user_blp)  # 사용자 API 연결
api.register_blueprint(board_blp)  # 게시판 API 연결

from flask import render_template  # HTML 파일을 웹에 보여주는 함수
@app.route('/manage-boards')  # URL 접속 시 boards.html 렌더링
def manage_boards():
    return render_template('boards.html')

@app.route('/manage-users')  # URL 접속 시 users.html 렌더링
def manage_users():
    return render_template('users.html')

# 서버를 실행하는 메인 블록
if __name__ == '__main__':
    with app.app_context():  # DB 작업 위해 Flask 앱 컨텍스트 사용
        print("여기 실행?")  # 콘솔 출력 테스트
        db.create_all()  # 테이블 자동 생성
    app.run(debug=True)  # 디버깅 모드로 실행
