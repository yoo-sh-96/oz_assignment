from db import db  # db.py에서 만든 SQLAlchemy 객체 불러오기

# 사용자 모델 정의 (users 테이블과 매핑됨)
class User(db.Model):  # Flask-SQLAlchemy 방식으로 모델 정의
    __tablename__ = "users"  # 실제 데이터베이스 테이블 이름 지정

    id = db.Column(db.Integer, primary_key=True)  # 기본키 ID (자동 증가 숫자)
    name = db.Column(db.String(100), unique=True, nullable=False)  # 사용자 이름 (중복X, 필수)
    email = db.Column(db.String(100), unique=True, nullable=False)  # 이메일 (중복X, 필수)

    # User ↔ Board 관계 설정 (1:N)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')  
    # 'Board' 모델과 연결됨. user.boards로 접근 가능

# 게시글 모델 정의 (boards 테이블과 매핑됨)
class Board(db.Model):
    __tablename__ = "boards"  # 실제 데이터베이스 테이블 이름

    id = db.Column(db.Integer, primary_key=True)  # 게시글 ID (기본키)
    title = db.Column(db.String(100), nullable=False)  # 제목 (필수)
    content = db.Column(db.String(200))  # 내용 (선택)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
    # 게시글 작성자 ID (users 테이블의 id 참조, 필수)

    author = db.relationship('User', back_populates='boards')  
    # 작성자 정보를 객체 형태로 접근 가능 (board.author.name 등)
