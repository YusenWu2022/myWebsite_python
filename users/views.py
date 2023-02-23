from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#限制访问一般在views中进行
# Create your views here.

def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    '''注册账号'''
    if request.method !='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            #自动登录到主页
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context={'form':form}
    return render(request,'users/register.html',context)
    #定义视图