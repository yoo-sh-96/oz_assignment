from flask import request, jsonify  # 사용자 요청 데이터 받기 / 응답을 JSON으로 변환
from flask.views import MethodView  # 클래스 기반 뷰 작성용 모듈
from flask_smorest import Blueprint  # API 분리 및 모듈화를 위한 Flask 확장 도구
from db import db  # DB 객체 import
from models import Board  # Board 모델 import

# 게시판 관련 API를 위한 블루프린트 객체 생성
board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# /board/ 경로에 대한 GET(조회), POST(생성) 메서드 처리
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):  # 전체 게시글 조회
        boards = Board.query.all()  # 모든 게시글 가져오기
        return jsonify([{
            "user_id": board.user_id,  # 작성자 ID
            "id": board.id,  # 게시글 ID
            "title": board.title,  # 제목
            "content": board.content,  # 내용
            "author": board.author.name  # 작성자 이름 (User와의 관계)
        } for board in boards])

    def post(self):  # 게시글 작성
        data = request.json  # 클라이언트로부터 받은 JSON 데이터
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_board)  # DB에 추가
        db.session.commit()  # 변경사항 저장
        return jsonify({"message": "Board created"}), 201  # 성공 메시지 반환

# /board/<board_id> 경로에 대한 GET, PUT, DELETE 처리
@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    def get(self, board_id):  # 특정 게시글 조회
        board = Board.query.get_or_404(board_id)  # 해당 ID 없으면 404 반환
        return jsonify({
            "title": board.title,
            "content": board.content,
            "author": board.author.name  # 관계 통해 사용자 이름 조회
        })

    def put(self, board_id):  # 게시글 수정
        board = Board.query.get_or_404(board_id)
        data = request.json  # 새 데이터 받기
        board.title = data['title']  # 제목 수정
        board.content = data['content']  # 내용 수정
        db.session.commit()  # 저장
        return jsonify({"message": "Board updated"})

    def delete(self, board_id):  # 게시글 삭제
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)  # 삭제 요청
        db.session.commit()  # 저장
        return jsonify({"message": "Board deleted"})