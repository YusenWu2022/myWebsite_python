"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
#from django.conf.urls import include,url
urlpatterns = [
    #只包含根目录的url和应用程序的url
    path('admin/', admin.site.urls),
    path('',include(('learning_logs.urls','learning_logs'),namespace='learning_logs')),
    #如果这里的应用程序没有用逗号隔开，就会报错“OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: '<frozen importlib._bootstrap>'”
    path('',include(('users.urls','users'),namespace='users')),
    #下面是有参数问题的代码
    #url(r'^admin/',include(admin.site.urls)),
    #url(r'',include('learning_logs.urls',namespace='learning_logs'))
    
]
