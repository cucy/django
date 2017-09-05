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


## 测试
```shell
>>> from django.test import Client
>>> c = Client()
>>> c.get("http://0.0.0.0:8000/hello-fn/").content
```
## 用户访问控制
### 用户是否登录装饰器
```python
@login_required
def simple_view(request):
	return HttpResponse()
# 等价于
def simple_view(request):
	return HttpResponse()
simple_view = login_required(simple_view)	
```
### 访问控制
- fbv
```python
@login_required(MyView.as_view())
```
- cbv
```python
from django.utils.decorators import method_decorator

class LoginRequiredMixin:
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
# 另一种方法
class LoginRequiredMixin:
	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)		
```
`另一种方法`
```python
# https://github.com/brack3t/django-braces

from braces.views import LoginRequiredMixin, AnonymousRequiredMixin

class UserProfileView(LoginRequiredMixin, DetailView):
# This view will be seen only if you are logged-in
	pass
		
class LoginFormView(AnonymousRequiredMixin, FormView):
	# This view will NOT be seen if you are loggedin
	authenticated_redirect_url = "/feed"
	
from braces.views import UserPassesTestMixin
class SomeStaffView(UserPassesTestMixin, TemplateView):
	def test_func(self, user):
		return user.is_staff
		
		
class CheckOwnerMixin:
	# To be used with classes derived from SingleObjectMixin
	def get_object(self, queryset=None):
		obj = super().get_object(queryset)
		if not obj.owner == self.request.user:
			raise PermissionDenied
		return obj		
```
## 上下文
```python
class FeedMixin(object):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["feed"] = models.Post.objects.viewable_posts(self.request.user)
		return context
		
class CtxView(StaticContextMixin, generic.TemplateView):
	template_name = "ctx.html"
	static_context = {"latest_profile": Profile.objects.latest('pk')}
```
## 返回json
```python
class PublicPostJSONView(generic.View):
	def get(self, request, *args, **kwargs):
		msgs = models.Post.objects.public_posts().values("posted_by_id", "message")[:5]
		return HttpResponse(list(msgs), content_type="application/json")	
```
```python
from braces.views import JSONResponseMixin

class PublicPostJSONView(JSONResponseMixin, generic.View):
    def get(self, request, *args, **kwargs):
        msgs = models.Post.objects.public_posts().values("posted_by_id", "message")[:5]
        return self.render_json_response(list(msgs))
```
## urls.py
```
urlpatterns = [
	url(r'^blog/', include('blog.urls', namespace='blog')),	
	url(r'^(?P<slug>\w+)/$', ArticleView.as_view(), name='article'),
]
```
```python



from django.core.urlresolvers import reverse
>>> print(reverse("home"))
"/"
>>> print(reverse("job_archive", kwargs={"pk":"1234"}))
"jobs/1234/"
```

## django-admin
```python
C:\Python27\Scripts\django-admin startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html myproj

```
## 自定义tags

create a `templatetags` directory inside an app
```python
# app/templatetags/nav.py
from django.core.urlresolvers import resolve
from django.template import Library

register = Library()

@register.simple_tag
def active_nav(request, url):
    url_name = resolve(request.path).url_name
    if url_name == url:
        return "active"
    return ""
```
```python
# settings.py
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (  'django.core.context_processors.request', )
```
```
# template
{# base.html #}
{% load nav %}
<ul class="nav nav-pills">
	<li class={% active_nav request 'active1' %}><a href="{% url 'active1' %}">Active 1</a></li>
	<li class={% active_nav request 'active2' %}><a href="{% url 'active2' %}">Active 2</a></li>
	<li class={% active_nav request 'active3' %}><a href="{% url 'active3' %}">Active 3</a></li>
</ul>
```

## Forms
### 简略的form
```python
# forms.py
from django import forms

class PersonDetailsForm(forms.Form):
	name = forms.CharField(max_length=100)
	age = forms.IntegerField()
	
	
>>> f = PersonDetailsForm()
>>> print(f.as_p())
<p><label for="id_name">Name:</label> <input id="id_name" maxlength="100" name="name" type="text" /></p>
<p><label for="id_age">Age:</label> <input id="id_age" name="age" type="number" /></p>
>>> f.is_bound
False

>>> g = PersonDetailsForm({"name": "Blitz", "age": "30"})
>>> print(g.as_p())
<p><label for="id_name">Name:</label> <input id="id_name" maxlength="100" name="name" type="text" value="Blitz" /></p>
<p><label for="id_age">Age:</label> <input id="id_age" name="age" type="number" value="30" /></p>
>>> g.is_bound
True	
	
```
- clean_data
```python
>>> fill = {"name": "Blitz", "age": "30"}
>>> g = PersonDetailsForm(fill)
>>> g.is_valid()
True
>>> g.cleaned_data
{'age': 30, 'name': 'Blitz'}
>>> type(g.cleaned_data["age"])
int
```
### 不同的方式显示form

| template            | code                                     | 浏览器展示                                    |
| ------------------- | ---------------------------------------- | ---------------------------------------- |
| {{ form.as_p }}     | `<p><label for="id_name">Name:</label> <input type="text" name="name" value="Blitz" id="id_name" required maxlength="100" /></p>` | ![form.as_p](https://github.com/cucy/django/raw/master/django_img/forms_as_p.jpg) |
| {{ form.as_ul }}    | `<li><label for="id_name">Name:</label> <input type="text" name="name" value="Blitz" id="id_name" required maxlength="100" /></li>` | ![form.as_ul](https://github.com/cucy/django/raw/master/django_img/forms_as_ul.jpg) |
| {{ form.as_table }} | `<tr><th><label for="id_name">Name:</label></th><td><input type="text" name="name" value="Blitz" id="id_name" required maxlength="100" /></td></tr>\n<tr><th><label for="id_age">Age:</label></th><td><input type="number" name="age" value="30" required id="id_age" /></td></tr>` | ![form.as_table](https://github.com/cucy/django/raw/master/django_img/forms_as_table.jpg) |

```html
<form method="post">
	{% csrf_token %}
	<table>{{ form.as_table }}</table>
	<input type="submit" value="Submit" />
</form>

```
- `django-crispy-forms`美化
```
# settings.py
CRISPY_TEMPLATE_PACK = "bootstrap3"
# forms.py
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit

class PersonDetailsForm(forms.Form):

    name = forms.CharField(max_length=100)

    age = forms.IntegerField()

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout.append(Submit('submit', 'Submit'))
```
### CBV forms的使用
```
# views.py
class ClassBasedFormView(generic.View):
    template_name = 'form.html'

    def get(self, request):
        form = PersonDetailsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PersonDetailsForm(request.POST)
        if form.is_valid():
            # Success! We can use form.cleaned_data now
            return redirect('success')
        else:
            # Invalid form! Reshow the form with error highlighted
            return render(request, self.template_name,{'form': form})
			
# ---  使用formview----
from django.core.urlresolvers import reverse_lazy

class GenericFormView(generic.FormView):
    template_name = 'form.html'
    form_class = PersonDetailsForm
    success_url = reverse_lazy("success")
```

###  `一些例子`
#### `动态表单`
```python
# forms.py
class PersonDetailsForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        upgrade = kwargs.pop("upgrade", False)
        super().__init__(*args, **kwargs)
        # Show first class option?
		
        if upgrade:
            self.fields["first_class"] = forms.BooleanField(label="Fly First Class?")
			
# views.py
class PersonDetailsEdit(generic.FormView):

    ...

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["upgrade"] = True
        return kwargs
```
#### `用户角色 表单`
```python
# forms.py
from braces.forms import UserKwargModelFormMixin

class PersonDetailsForm(UserKwargModelFormMixin, forms.Form):
    ...
	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Are you a member of the VIP group?
        if self.user.groups.filter(name="VIP").exists():
            self.fields["first_class"] = forms.BooleanField(label="Fly First Class?")
			
# views.py
class VIPCheckFormView(LoginRequiredMixin, UserFormKwargsMixin, generic.FormView):

   form_class = PersonDetailsForm
    ...
	
```
#### `一个页面多个modle form需要显示`
```python
# forms.py
class SubscribeForm(forms.Form):
    email = forms.EmailField()
	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('subscribe_butn', 'Subscribe'))
# views.py
from .forms import SubscribeForm, UnSubscribeForm

class NewsletterView(generic.TemplateView):
    subcribe_form_class = SubscribeForm
    unsubcribe_form_class = UnSubscribeForm
    template_name = "newsletter.html"

    def get(self, request, *args, **kwargs):
        kwargs.setdefault("subscribe_form", self.subcribe_form_class())
        kwargs.setdefault("unsubscribe_form", self.unsubcribe_form_class())
        return super().get(request, *args, **kwargs)
		
	def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
            'files': self.request.FILES,
        }

        if "subscribe_butn" in request.POST:
            form = self.subcribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,subscribe_form=form)
            return redirect("success_form1")

        elif "unsubscribe_butn" in request.POST:
            form = self.unsubcribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,unsubscribe_form=form)
            return redirect("success_form2")
			
        return super().get(request)
```
#### ` CRUD views`
```python
# models.py
class ImportantDate(models.Model):
    date = models.DateField()
    desc = models.CharField(max_length=100)
	
    def get_absolute_url(self):
        return reverse('impdate_detail', args=[str(self.pk)])

# forms.py
from django import forms
from . import models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ImportantDateForm(forms.ModelForm):
	class Meta:
        model = models.ImportantDate
        fields = ["date", "desc"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))		
		
# views.py
from django.core.urlresolvers import reverse_lazyfrom . import forms

class ImpDateDetail(generic.DetailView):
    model = models.ImportantDate

class ImpDateCreate(generic.CreateView):
    model = models.ImportantDate
    form_class = forms.ImportantDateForm

class ImpDateUpdate(generic.UpdateView):
    model = models.ImportantDate
    form_class = forms.ImportantDateForm

class ImpDateDelete(generic.DeleteView):
    model = models.ImportantDate
    success_url = reverse_lazy("impdate_list")
	
# urls.py
urlpatterns = [ 
# ...
	url(r'^impdates/create/$', pviews.ImpDateCreate.as_view(), name="impdate_create"),
	url(r'^impdates/(?P<pk>\d+)/$',pviews.ImpDateDetail.as_view(), name="impdate_detail"),
	url(r'^impdates/(?P<pk>\d+)/update/$',pviews.ImpDateUpdate.as_view(), name="impdate_update"),
	url(r'^impdates/(?P<pk>\d+)/delete/$',pviews.ImpDateDelete.as_view(), name="impdate_delete"),
# ...
]	
```



