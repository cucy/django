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