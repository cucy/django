from django.contrib import admin
from hello.models import *
# Register your models here.

# 第一种方法
# class PublisherAdmin(admin.ModelAdmin):
#     list_display = ('name', 'country', 'state_province', 'city')

# 第二种方法
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'state_province', 'city')

admin.site.register(Author)
admin.site.register(AuthorDetail)
# admin.site.register(Publisher, PublisherAdmin) # 一种方法
admin.site.register(Book)