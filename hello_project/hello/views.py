from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def hello(request):
    user_list = User.objects.all() # 从用户模型查看所有的用户
    return render(request, 'table.html', {'user_list': user_list})
