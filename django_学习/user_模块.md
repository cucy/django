
## django.contrib.auth.views
`属性集`
settings.py中设置
- LOGOUT_URL
- LOGIN_REDIRECT_URL
`方法集`
- login()
- logout()
- redirect_to_login()
- logout_then_login()


## 有用的示例
```python
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
```
`创建用户`
```python
 User.objects.create_user(
	'andrew' , 
	'django@jambonsw.com' ,
	'hunter2' 
) 
User.objects.values()
Out[4]: <QuerySet [{'username': 'andrew', 'email': 'django@jambonsw.com', 'is_active': True, 'last_name': '', 'is_staff': False, 'first_name': '', 'id': 1, 'last_login': None, 'date_joined': datetime.datetime(2017, 9, 6, 3, 46, 56, 354294, tzinfo=<UTC>), 'password': 'pbkdf2_sha256$36000$seq7heY1Mm2Q$DEml06NlYnusJ1bVD3JCAZIXwtsH2QAkYA1VKFPKFc4=', 'is_superuser': False}]>

# admin
In [15]: andrew = User.objects.create_superuser(
    ...: "andrew",
    ...: "django@qq.com",
    ...: "hunter2")
```
`检查用户`
```python
andrew = User.objects.all()[0]
In [3]: andrew.is_active # 是否能登入网站
Out[3]: True

In [4]: andrew.is_staff # 是否能登录admin后台的网站
Out[4]: False

In [5]: andrew.is_superuser
Out[5]: False

In [7]: andrew.get_username()
Out[7]: 'andrew'

In [8]: andrew.is_authenticated()
Out[8]: True
```
### example
`urls.py`
```python
from django.contrib.auth import urls as auth_urls
urlpatterns = [
    url(r'^user/', include(auth_urls)),
	]
```
`template`
```hrml
# templates/registration/logged_out.html
{% extends parent_template|default:"base.html" %}

{% block title %}
{{ block.super }} - Logged Out
{% endblock %}

{% block content %}
<p>You've successfully logged out.</p>
{% endblock %}
```


## 权限模块
```
In [1]: from django.contrib.contenttypes.models import ContentType

In [3]: ContentType.objects.values()
Out[3]: <QuerySet [{'model': 'logentry', 'app_label': 'admin', 'id': 1}, {'model': 'user', 'app_label': 'auth', 'id': 2}, {'model': 'group', 'app_label': 'auth', 'id': 3}, {'model': 'permission', 'app_label': 'auth', 'id': 4}, {'model': 'contenttype', 'app_label': 'contenttypes', 'id': 5}, {'model': 'flatpage', 'app_label': 'flatpages', 'id': 6}, {'model': 'session', 'app_label': 'sessions', 'id': 7}, {'model': 'site', 'app_label': 'sites', 'id': 8}, {'model': 'newslink', 'app_label': 'organizer', 'id': 9}, {'model': 'tag', 'app_label': 'organizer', 'id': 10}, {'model': 'startup', 'app_label': 'organizer', 'id': 11}, {'model': 'post', 'app_label': 'blog', 'id': 12}]>
```
### 获取model的权限
```python
In [9]: post_ct = ContentType.objects.get(app_label= 'blog' )

In [10]: Post = post_ct.model_class()

In [11]: Post.objects.count()
Out[11]: 6
```
### 检查用户是否有权限
```python
from django.contrib.auth import get_user_model
In [14]: andrew = User.objects.get(username= 'andrew' )

In [15]: andrew.is_superuser
Out[15]: True

In [16]: andrew.has_perm('blog.add_post')
Out[16]: True

In [17]: andrew.has_perm('blog.change_post')
Out[17]: True

In [18]: andrew.has_perm('blog.delete_post')
Out[18]: True
```
###添加权限
- 1.
```python 
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from blog.models import Post

blog_content_type = ContentType.objects.get_for_model(Post)
Permission.objects.filter(content_type= blog_content_type)

new_permission = Permission.objects.create(
codename= 'view_future_post' ,
name= 'Can view unpublished Post' ,
content_type= blog_content_type)

In [29]: new_permission
Out[29]: <Permission: blog | blog post | Can view unpublished Post>
```
- 2. model中添加
```python
class Meta:
		... 
        permissions = (
            ("view_future_post",
             "Can view unpublished Post"),
        )
		...
		
		
# 同步数据库
$ ./manage.py makemigrations --name= add_view_future_post_permission blog
$ ./manage.py migrate

# 查看
In [31]: Permission.objects.get(codename= 'view_future_post' )
Out[31]: <Permission: blog | blog post | Can view unpublished Post>
```
## 组权限
```python
In [32]: from django.contrib.auth.models import Group

In [33]: Group.objects.all()
Out[33]: <QuerySet []>
# 添加组
In [34]:  Group.objects.create(name= 'contributors' )
Out[34]: <Group: contributors>

In [38]: Group.objects.filter(name=  'contributors' ).values()
Out[38]: <QuerySet [{'name': 'contributors', 'id': 1}]>

# 组和权限进行关联
Permission.objects.get(codename= 'view_future_post' )

In [45]: contributor = Group.objects.get(name=  'contributors' )

In [46]: contributor.permissions.add(
    ...:  Permission.objects.get(codename= 'view_future_post' ),
    ...:  Permission.objects.get(codename= 'add_post' )
    ...: )
    
In [47]: contributor.permissions.all()
Out[47]: <QuerySet [<Permission: blog | blog post | Can add blog post>, <Permission: blog | blog post | Can view unpublished Post>]>

# 用户添加到组
In [51]: ada = User.objects.get(username= 'ada' )

In [52]: ada.groups
Out[52]: <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0x6f2eda0>

In [53]: ada.groups.add(contributor)

In [54]: ada.groups.all()
Out[54]: <QuerySet [<Group: contributors>]>
# 查看用户所有的权限
In [63]:  ada.get_group_permissions()
Out[63]: {'blog.add_post', 'blog.view_future_post'}

In [65]:  ada.get_all_permissions()
Out[65]: {'blog.add_post', 'blog.view_future_post'}

```

## views中权限
```python
# urls.py
from django.contrib.auth.decorators import login_required

urlpatterns = [
... 
    url(r'^create/$',
        login_required(
            TagCreate.as_view()),
        name='organizer_tag_create'),
		]\
		
		
```
```python
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class TagCreate(CreateView):
	...
	@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(
            request, *args, **kwargs)

# 另一种
from django.contrib.auth.decorators import  permission_required	

class TagCreate(CreateView):
	... ... 
    @method_decorator(login_required)
    @method_decorator(permission_required( 'organizer.add_tag', raise_exception=True, ))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)
	
```
#### 自定义权限装饰器
- 函数权限装饰器
```python
# decorators.py
from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect


def custom_login_required(view):
    # view argument must be a function

    def new_view(request, *args, **kwargs):
        user = get_user(request)
        if user.is_authenticated():
            return view(request, *args, **kwargs)
        else:
            url = '{}?next={}'.format(
                settings.LOGIN_URL,
                request.path)
            return redirect(url)

    return new_view

# views.py
class TagUpdate (UpdateView):
	... 
	
	@method_decorator (custom_login_required)
	def dispatch (self , request, * args, ** kwargs):
		return super (). dispatch( request, * args, ** kwargs)	
```
- 类装饰器
```python
# decorators.py
from django.contrib.auth.decorators import (
    login_required, permission_required)
from django.core.exceptions import \
    ImproperlyConfigured
from django.utils.decorators import \
    method_decorator
from django.views.generic import View


def require_authenticated_permission(permission):

    def decorator(cls):
        if (not isinstance(cls, type)
                or not issubclass(cls, View)):
            raise ImproperlyConfigured(
                "require_authenticated_permission"
                " must be applied to subclasses "
                "of View class.")
        check_auth = (
            method_decorator(login_required))
        check_perm = (
            method_decorator(
                permission_required(
                    permission,
                    raise_exception=True)))

        cls.dispatch = (
            check_auth(check_perm(cls.dispatch)))
        return cls

    return decorator

# views.py
from user.decorators import ( class_login_required, require_authenticated_permission)


@require_authenticated_permission('organizer.add_tag')
class TagUpdate (UpdateView):
	form_class = TagForm
	model = Tag	
```

