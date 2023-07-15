from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # on_delete=models.SET_NULL => 유저가 회원탈퇴를 했을 때 게시글을 지우지 않고 유지(게시자는 알수없는 유저)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
