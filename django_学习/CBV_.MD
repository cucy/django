
# reverse 函数
```
In [26]: from django.core.urlresolvers import reverse

In [27]: reverse('organizer_tag_list' )
Out[27]: '/tag/'

In [28]: from django.template import Template, Context

In [29]: code = "{% url 'organizer_tag_list' %}"

In [30]: template = Template(code)

In [31]: template.render(Context())
Out[31]: '/tag/'

# slug关键字
In [33]: from django.core.urlresolvers import reverse

In [34]: reverse('organizer_tag_detail' , args= ['django' ])
Out[34]: '/tag/django/'

In [35]: reverse('organizer_tag_detail' , kwargs= {'slug' : 'django' })
Out[35]: '/tag/django/'

# slug关键字在模板中的应用
#-----------------------------------
In [36]: from django.template import Template, Context

In [37]: code = "{% url 'organizer_tag_detail' 'web' %}"

In [38]: template = Template(code)

In [39]: template. render(Context())
Out[39]: '/tag/web/'

In [40]: code = "{% url 'organizer_tag_detail' slug='web' %}"

In [41]: template = Template(code)

In [42]: template. render(Context())
Out[42]: '/tag/web/'
#
In [49]: from django.template import Template, Context
    ...: from organizer.models import Tag
    ...: django_tag = Tag.objects.get(slug__iexact= 'django' )
    ...: context = Context({'tag' : django_tag})
    ...: code = "{% url 'organizer_tag_detail' tag.slug %}"
    ...: template = Template(code)
    ...: template.render(context)
    ...:
Out[49]: '/tag/django/'
#------------------------------------------

# slug关键字在 views
In [43]: from django.core.urlresolvers import reverse

In [44]: from organizer.models import Tag

In [45]: django_tag = Tag.objects.get(slug__iexact= 'django' )

In [46]: reverse('organizer_tag_detail' , kwargs= {'slug' : django_tag. slug})
Out[46]: '/tag/django/'
```