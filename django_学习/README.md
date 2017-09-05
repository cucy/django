## django请求生命周期
![django一个请求生命周期](https://github.com/cucy/django/raw/master/django_img/django_request_life.jpg)
--- 
- 1浏览器发起url请求
- 2web服务器分析请求对象(nginx、httpd...)静态文件直接从文件系统中返回，否则送给WSGI server进行处理
- 3通过一层或者多层转发后(WSGI)至python环境,安装有django应用环境进行处理
- 4请求url进行urls.py配置进行匹配,生成一个http request python对象，送到对应的视图(view)
- 5view通常要做以下事情
- 5a通过model与数据库进行交互
- ​5b渲染成HTML或者其他格式
- 5c构造响应HttpResponse 
- 5d抛出异常
- 6通过WSGI返回HttpResponse给web server
- 7用户浏览器进行页面渲染

## 快速启动一个python环境
- 环境准备
```shell
$ python3 -m venv sbenv

$ source sbenv/bin/activate

$ export PATH="`pwd`/sbenv/local/bin:$PATH"
```
- 版本
```shell
$ git clone xxxx

$ cd superbook

$ pip install -r requirements.txt
```
- 同步数据库
```shell
$ cd xxx

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver
```
## 模型
`Django`通过面向对象方式处理数据库，每个类引用数据表，每个属性引用列，通过API直接操作数据库
## 视图

| **Type** | **Class Name**   | **Description**                          |
| -------- | ---------------- | ---------------------------------------- |
| Base     | View             | This is the parent of all views. It performs dispatch and sanity checks. |
| Base     | TemplateView     | This renders a template. It exposes the URLConf keywords into context. |
| Base     | RedirectView     | This redirects on any GET request.       |
| List     | ListView         | This renders any iterable of items, such as a queryset. |
| Detail   | DetailView       | This renders an item based on pk or slug from URLConf. |
| Edit     | FormView         | This renders and processes a form.       |
| Edit     | CreateView       | This renders and processes a form for creating new objects. |
| Edit     | UpdateView       | This renders and processes a form for updating an object. |
| Edit     | DeleteView       | This renders and processes a form for deleting an object. |
| Date     | ArchiveIndexView | This renders a list of objects with a date field, the latest being the first. |
| Date     | YearArchiveView  | This renders a list of objects on year given by URLConf. |
| Date     | MonthArchiveView | This renders a list of objects on a year and month. |
| Date     | WeekArchiveView  | This renders a list of objects on a year and week number. |
| Date     | DayArchiveView   | This renders a list of objects on a year, month, and day. |
| Date     | TodayArchiveView | This renders a list of objects on today's date. |
| Date     | DateDetailView   | This renders an object on a year, month, and day identified by its pk or slug. |