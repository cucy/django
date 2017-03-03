"""hello_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from hello import views


urlpatterns = [
    url(r'^hello/$', 'views.hello', {'a': '123'}, 'hello','hello'),
    url(r'^test/(?P<id>\d{2})/(?P<key>\w+)/$', 'hello.views.test')
]

# url(正则表达式, view函数,参数,别名,前缀)

#  两种方法
# 1、函数方法方式      url(r'^hello/$', views.hello)
# 2、字符串方式       url(r'^hello/$', 'hello.views.hello')