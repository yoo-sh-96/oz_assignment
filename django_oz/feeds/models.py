from django.db import models
from common.models import CommonModel

# 제목, 내용, 작성자(User)
# Feed 와 User의 관계
# User -> Feed, Feed, Feed (o)
# Feed -> User, User, User (x)
# User:Feed = 1:N

class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)