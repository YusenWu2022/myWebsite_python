from django.conf.urls import url

from . import views

urlpatterns=[
    #主页
    url(r'^$',views.index,name='index'),
    url(r'^topic/$',views.topics,name='topics'),
    #特定项目的页面，直接传参匹配
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #用于添加新主题的网页
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
     #添加新条目
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    #记得写完一项加逗号
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
]