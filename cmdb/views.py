from django.shortcuts import render
from . import models


# from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    #    return HttpResponse('hello world!')
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 添加数据到数据表
        models.UserInfo.objects.create(user=username, pwd=password)
    # 从数据库读取所有数据
    user_list = models.UserInfo.objects.all()

    return render(request, 'cmdb/index.html', {"data": user_list})
