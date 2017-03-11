from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def hello(request, a):
    user_list = User.objects.all() # 从用户模型查看所有的用户
    # print(user_list.query)
    return render(request,'table.html', {'user_list': user_list})


def test(request):
    return render(request, 'table.html')

def add_publisher(request):
    if request.method == 'POST':
        # 如果post提交， 去接收用户传过来的数据
        print(request.POST)
    else:
        return render(request, 'add_publisher.html', locals())


