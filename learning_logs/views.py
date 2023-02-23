from django.shortcuts import render,get_object_or_404
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    '''学习笔记的首页'''
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    '''显示所有主题'''
    #添加了过滤器，显示相关的主题
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    '''单个条目页面'''
    #topic=Topic.objects.get(id=topic_id)
    topic=get_object_or_404(Topic,id=topic_id)
    if topic.owner != request.user:
        raise Http404
        #检查是否越权访问
    entries=topic.entry_set.order_by('id')#特殊的，用id 代替date_added 否则会参数错误
    context={'topic':topic,'entries':entries}#主题和条目的字典
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method!='POST':
        form=TopicForm()
    else :
        form=TopicForm(request.POST)
        if form.is_valid():
            # form.save()
            #关键步骤：下面添加了关联主题和作者的代码。
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            #reverse得到url，Http...direct重定向到指定url
    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    '''添加新条目'''
    topic=Topic.objects.get(id=topic_id)
    if request.method !='POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            if new_entry.topic.owner != request.user:
                raise Http404
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)
#注：new_entry 不需要关联作者（用户），因为已经和topic关联，topic又关联于用户了

@login_required
def edit_entry(request,entry_id):
    '''修改已有条目'''
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner != request.user:
        raise Http404
        #保护措施
    if request.method !='POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)


        





