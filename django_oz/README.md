#  👨‍💻학습내용
# 1. Django란?
   - 특징 :
     
     - Django는 Python 기반의 웹 프레임워크로, 고수준의 웹 개발을 위한 기능을 포괄적으로 제공합니다.
     
     - 대표적인 모듈로는 ORM(객체 관계 매핑), MTV(Model-Template-View) 아키텍처, Django REST framework(RESTful API 개발) 등이 있습니다.

   - 장점 :
     
     - 기본적인 기능들이 이미 내장되어 있어 빠르게 개발을 시작할 수 있습니다.
     
     - 강력한 ORM 기능으로 데이터베이스 작업이 편리합니다.
---

# 2. Django 프로젝트 세팅
   - Poetry 설치
     ```
     brew install poetry
     poetry --version
     ```

   - Poetry 세팅
      ```
      ## 폴더 생성
      mkdir oz-backend-django

      ## 폴더 이동
      cd oz-backend-django
      
      ## poetry 초기화
      poetry init
      
      ## vsc 열기
      code .
      
      # django 설치
      poetry add Django
      ```
      
   - 가상환경에서 Django 실행
      ```
      # 현재 폴더에서 프로젝트 생성 ( . 은 현재 경로)
	    django-admin startproject config .
      ```

   - admin 명령어
     - django-admin startproject myproject
        - 새로운 Django 프로젝트를 생성합니다.

     - django-admin startapp myapp
        - 프로젝트 내에 새로운 애플리케이션을 생성합니다.


   - Django 서버 실행
     ```
     python manage.py runserver # 장고 서버 실행
     python manage.py migrate # migtation 문제 해결
     ```
---

# 3. URL, VIEW 개념 
  - URL Dispatcher (urls.py)
    
    - Django의 URL Dispatcher는 Django 웹 프레임워크의 핵심 구성 요소 중 하나로, 웹 요청을 처리하고
      
      해당 요청에 맞는 View 함수로 라우팅하는 역할을 합니다. 즉, 사용자가 웹 브라우저에서 URL을 요청할 때,
        
      URL Dispatcher는 이 URL을 분석하여 정의된 URL 패턴 중에서 일치하는 패턴을 찾고, 해당 패턴에 연결된 View 함수를 호출합니다.

  - URL Dispatcher의 작동 방식
    - URL 패턴 정의: Django 프로젝트의 urls.py 파일에는 URL 패턴이 정의됩니다. 이 패턴은 특정 URL과 이 URL이 호출할 View 함수를 매핑합니다.
    - URL 매칭: 사용자가 웹사이트에 접근할 때, URL Dispatcher는 요청된 URL을 urls.py에 정의된 패턴과 순차적으로 비교합니다.
    - View 함수 호출: 일치하는 URL 패턴을 찾으면, URL Dispatcher는 해당 URL 패턴에 연결된 View 함수를 호출합니다. View 함수는 HTTP 요청을 처리하고 응답을 반환합니다.
    - 변수 전달: URL 패턴에는 변수를 포함시킬 수 있습니다. 이 변수들은 동적으로 변경되는 URL 부분을 처리하고, 이 값을 View 함수에 인자로 전달할 수 있습니다.
   
  - URL & VIEW 설정
    config/urls.py
    ```
    from django.contrib import admin
    from django.urls import path
    from feeds import views

    urlpatterns = [
      path("admin/", admin.site.urls),
		  path("feeds/", views.show_feed),
		  path("feeds/all", views.all_feed),
	  	path("feeds/<int:feed_id>/<str:feed_content>/", views.one_feed),
    ]
    ```

    feeds/views.py
    ```
    from django.shortcuts import render
    from django.http import HttpResponse

    def show_feed(request):
	    return HttpResponse("show feed")

    def one_feed(request, feed_id, feed_content):
    	return HttpResponse(f"feed id: {feed_id}, {feed_content}")

    def all_feed(request):
    	return HttpResponse("all feed")
    ```
---

# 4. Model 개념 
  - 모델의 기본 개념
      - 클래스로서의 모델: Django에서 모델은 django.db.models.Model 클래스를 상속받아 정의됩니다. 모델 클래스의 각 속성은 데이터베이스 테이블의 열(column)에 해당합니다.
      - 필드 정의: 모델 안에 다양한 필드 타입(CharField, IntegerField 등)을 정의하여 데이터베이스 테이블의 구조를 결정합니다. 필드 타입은 저장하고자 하는 데이터의 종류(문자열, 숫자, 날짜 등)에 따라 결정됩니다.
      - 데이터베이스 테이블과의 매핑: Django는 모델 클래스를 기반으로 데이터베이스 테이블을 생성합니다. 클래스 이름이 테이블 이름으로 사용되며, 클래스의 필드가 테이블의 열로 변환됩니다.
      - ORM 기능: 모델을 통해 CRUD (Create, Read, Update, Delete) 작업을 SQL 쿼리를 작성하지 않고도 수행할 수 있습니다. Django ORM은 이러한 작업을 Python 코드로 간소화합니다.

  - 모델 생성
      ```
      > python manage.py startapp boards # board라는 모델을 생성
      ```
  - boards/models.py 에서 모델 정의
      ```
      class Board(models.Model):
        title = models.CharField(max_length=30)
        content = models.TextField()
        date = models.DateTimeField(auto_now_add=True)
        likes = models.PositiveIntegerField(default=0)
        reviews = models.PositiveIntegerField(default=0)
      ```
  - config/settings.py
      ```
      INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "boards.apps.BoardsConfig" # 추가
      ]
      ```
  - boards/admin.py
    ```
    from django.contrib import admin
    from .models import Board

    @admin.register(Board)
    class BoardAdmin(admin.ModelAdmin):
    	pass
    ```
    - Django가 DB와 아직 소통하기 전

  - makemigrations / migrate
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
---

# 5. ORM
  - ORM (Object-Relational Mapping) 이란?
    - 객체(Object) - 장고
    - 관계형(Relational)데이터베이스 DB - RDBMS
    - 위 2개를 Mapping(연결) 시켜주는 것

  - 주요 메소드
    - filter(): 조건에 맞는 객체들만 포함하는 새 QuerySet을 반환합니다.
    - exclude(): 주어진 조건을 만족하지 않는 객체들만 포함하는 새 QuerySet을 반환합니다.
    - annotate(): 집계 함수를 적용하거나 쿼리 결과에 계산된 필드를 추가합니다.
    - aggregate(): 전체 QuerySet에 대한 집계(합계, 평균 등)를 계산합니다.
    - order_by(): QuerySet의 결과를 특정 필드에 따라 정렬합니다.
    - all(): 데이터베이스의 모든 레코드를 포함하는 QuerySet을 반환합니다.
    - get(): 단일 객체를 반환합니다. 조건에 맞는 객체가 없거나 둘 이상인 경우 예외를 발생시킵니다.
---

#  ORM 실습
<img width="1504" alt="Image" src="https://github.com/user-attachments/assets/e84bc6f0-bc15-425c-a788-6e333f04af1f" />
