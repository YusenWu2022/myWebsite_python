from django.conf.urls import url
#from django.contrib.auth.views import login   这是早期版本的写法，已经弃用，需要大更新
#现在需要使用Loginview来调用，否则无法导入旧版本:
from django.contrib.auth.views import LoginView
#默认视图views，只需要自己写模板调用

from . import views

urlpatterns=[
    #登录界面
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    #url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    #这是更新版本的代码
    #使用官方默认的login作为view视图
    #注销,自己写个view
    url(r'^logout/$',views.logout_view,name='logout'),
    #也可以使用官方的LogoutView这样会出来一个多余的注销页面
    #注册页面
    url(r'^register/$',views.register,name='register'),
]