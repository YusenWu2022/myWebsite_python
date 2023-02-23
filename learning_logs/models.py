from django.db import models
from django.contrib.auth.models import User
#create your models here

class Topic(models.Model):
    '用户学习的主题'
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    #添加外键
    #注意类比，遇到on_delete问题时候类比之前entry与topic关联时候加的参数（17行）
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):
    '存储的具体学习记录'
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    data_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='entries'
    def __str__(self):
        return self.text[:50]+'...'



