## 基本
```python
In [1]: from django.template import Template, Context

In [2]: template = Template('Hi, my name is {{ name }}.' )

In [3]: context = Context({'name' : 'Andrew' })

In [4]: template.render(context)
Out[4]: 'Hi, my name is Andrew.'

In [5]: template.render(Context())
Out[5]: 'Hi, my name is .'

In [8]: template.render(Context({'name' : 'Andrew' }))
Out[8]: 'Hi, my name is Andrew.'
```
## html模板
```python
# 准备模板
In [9]: template = Template(
   ...:  '{{ ml.exclaim }}! \n '
   ...:  'she said {{ ml.adverb }} \n '
   ...:  'as she jumped into her convertible {{ ml.noun1 }} \n '
   ...:  'and drove off with her {{ ml.noun2 }}. \n '
   ...:  )
   
# 准备数据
In [10]: mad_lib = {
    ...:  'exclaim' :'Ouch' ,
    ...:  'adverb' :'dutifully' ,
    ...:  'noun1' :'boat' ,
    ...:  'noun2' :'pineapple' ,
    ...:  }
In [11]: context = Context({'ml' : mad_lib})

# 渲染
In [12]: template.render(context)
Out[12]: 'Ouch! \n she said dutifully \n as she jumped into her convertible boat \n and drove off with her pineapple. \n '	
```
## 获取模板函数 （有错误）
```python
from django.template import Template, Context
# 准备模板
In [1]: from django.template import loader
In [2]: template = loader.get_template('organizer/tag_list.html' )

# 准备数据
In [5]: best_list = {'name' : 'Pirates' }
In [6]: context = Context({'tag_list' : best_list})
# 渲染
In [9]: template.render(context)
```
## 使用models中的数据进行渲染 （有错误）
```python
# 导入
from django.template import Template, Context
from django.template import loader

from organizer.models import Tag
Tag.objects.all()
template = loader.get_template('organizer/tag_list.html' )
# 数据
c = Context()
c['tag_list']  = Tag.objects.all()
# 渲染
template.render(c)
```
