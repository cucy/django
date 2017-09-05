## 创建
### 创建单个对象
```python
In [13]: Tag.objects.create(name= 'Video Games' , slug= 'video-games')
Out[13]: <Tag: Video Games>
```
### 创建多个对象
```python
In [14]: Tag.objects.bulk_create([
    ...:  Tag(name= 'Django' , slug= 'django' ),
    ...:  Tag(name= 'Mobile' , slug= 'mobile' ),
    ...:  Tag(name= 'Web' , slug= 'web' ),
    ...: ])
Out[14]: [<Tag: Django>, <Tag: Mobile>, <Tag: Web>]
```

```python
In [61]: jb = Startup.objects.create(
    ...:     name= 'JamBon Software' ,
    ...:     slug= 'jambon-software' ,
    ...:     contact= 'django@jambonsw.com' ,
    ...:     description= 'Web and Mobile Consulting. \n\n ''Django Tutoring. \n ',
    ...:     founded_date= date(2013,1,18),
    ...:     website= 'https://jambonsw.com/' ,
    ...: )
		
```

## R 相关
### `queryset 和返回实例对象的区别`
```python
In [28]: Tag.objects.get(slug='django')
Out[28]: <Tag: Django>

In [29]: type(Tag.objects.all())
Out[29]: django.db.models.query.QuerySet

In [30]: type(Tag.objects.get(slug='django'))
Out[30]: organizer.models.Tag

In [34]: try:
    ...:     Tag.objects.get(slug='Django1')
    ...: except Tag.DoesNotExist as e:
    ...:     print(e)
    ...:
Tag matching query does not exist.
```
### 单词匹配
```python 
# 非精确
# SQL: LIKE 'DJanGO'
In [37]: Tag.objects.get(slug__iexact='DJanGO')
Out[37]: <Tag: Django>

# 精确
# SQL:  WHERE `organizer_tag`.`slug` = 'DJanGO'
In [45]: Tag.objects.get(slug__exact='DJanGO')
Out[45]: <Tag: Django>
```
### 正则 contains
```python
# SQL: WHERE `organizer_tag`.`slug` LIKE BINARY '%o%'
In [47]: try:
    ...:     Tag.objects.get(slug__contains='o')
    ...: except Tag.MultipleObjectsReturned as e:
    ...:     print(e)
    ...:
get() returned more than one Tag -- it returned 4!
```
### filter
```python
In [50]: Tag.objects.filter(slug__contains='o').order_by('-name')
Out[50]: <QuerySet [<Tag: Video Games>, <Tag: Mobile>, <Tag: Education>, <Tag: Django>]>
```

### value_list
```python
In [51]: Tag.objects.values_list()
Out[51]: <QuerySet [(4, 'Django', 'django'), (2, 'Education', 'education'), (5, 'Mobile', 'mobile'), (3, 'Video Games', 'video-games'), (6, 'Web', 'web')]>

In [54]: Tag.objects.values_list('name')
Out[54]: <QuerySet [('Django',), ('Education',), ('Mobile',), ('Video Games',), ('Web',)]>

In [55]: Tag.objects.values_list('name', flat=True)
Out[55]: <QuerySet ['Django', 'Education', 'Mobile', 'Video Games', 'Web']>
```

```python
In [21]: Tag.objects.all()[0]
Out[21]: <Tag: Django>

In [22]: type(Tag.objects.all())
Out[22]: django.db.models.query.QuerySet

In [23]: try:
    ...:     edut.objects
    ...: except AttributeError as e:
    ...:     print(e)
    ...:
Manager isn't accessible via Tag instances

In [24]: Tag.objects.count()
Out[24]: 5
```