# django

## 创建工程(project)
django-admin.exe startproject hello_project

## 创建应用
- 进入工程创建应用
cd hello_project/
django-admin.exe startapp hello

## manage.py
是对django-admin的一个封装， 每个django项目都会有一个manage.py
```
$ python3 manage.py help

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```
- django默认会创建一个admin的后台但是无法使用,必须生成
```
manage.py makemigrations
No changes detected
生成数据库同步的脚本
manage.py migrate  # 新命令进行同步
Operations to perform:
  Apply all migrations: auth, contenttypes, sessions, admin
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying sessions.0001_initial... OK

```

- 创建超级管理员
```
python manage.py createsuperuser
Username (leave blank to use 'zhourudong'): admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```
- 访问管理后台
**http://127.0.0.1:5001/admin/**
- 修改用户密码
```
python manage.py   changepassword
```

## 目录结构
```
.
├── db.sqlite3
├── hello  # hello app(一个大的项目会有不同的app, 不同的app负责不同的功能模块，一个app负责一个功能 )
│   ├── admin.py  配置后台管理的文件
│   ├── apps.py   app配置
│   ├── __init__.py
│   ├── migrations      数据库同步的脚本目录
│   │   └── __init__.py
│   ├── models.py     模型代码配置文件，配置数据库模型
│   ├── tests.py      单元测试
│   └── views.py      业务代码主要位置
├── hello_project
│   ├── __init__.py
│   ├── __pycache__  存放缓存文件
│   ├── settings.py  静态文件设置
│   ├── urls.py      网页地址配置文件
│   └── wsgi.py      协议的配置文件， 在项目部署使用的时候会用到这个文件
└── manage.py
```

## 步骤
### 在view定义一个请求处理的函数
```
1.
setting.py 增加hello app的名字
-----
2、  views.py定义请求处理函数返回模板渲染
3、  static存放js css 静态文件， templates模版目录
4、  urls.py 定义访问的地址
        有多种方法定义url, url进行模式匹配，
        url(r'^hello$', views.hello, name='hello') # name为别名
        hello 定义到了views。hello函数进行处理


-------------
C:\3.6\django\Lib\site-packages\django\contrib\auth\models.py

from django.contrib.auth.models import User
导入用户User模块,进行调用
```

## mvt

### 修改模板静态文件存放路径
```
settings.py # TEMPLATES ['templates']配置目录

settings.py # 静态文件修改 STATICFILES_DIRS =( os.path.join(BASE_DIR,'static'), )
```

### 调整url
```
1、引入include
    from django.conf.urls import url, include
    url(r'^/', include('hello.urls'))
2、
    在app下创建 urls.py文件

```

## urls.py
```
ROOT_URLCONF = 'hello_project.urls' # 定义url的分发器
# 使用
模式匹配代替url已经不推荐使用


# url(正则表达式, view函数,参数,别名,前缀)

#  两种方法
# 1、函数方法方式      url(r'^hello/$', views.hello)
# 2、字符串方式       url(r'^hello/$', 'hello.views.hello')
```

## 获取get/ POST请求参数
``` 
request.GET.get('key')
request.POST.post('key')
```

## 连接mysql
```apple js
pip install pymysql
连接mysql需要先导入

创建数据库
python  manage.py  makemigrations
python manage.py migrate  （1.9以前syncdb）
```

## orm
```mysql
models.py 
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    address = models.CharField("地址", max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)

class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男'),(1, '女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2,default=10)
    
    
重新同步数据库
python  manage.py  makemigrations
```

## orm常用操作
```mysql


```