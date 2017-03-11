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
    search_fields = ("name", "city") # 按照name来搜索
    list_filter = ("state_province",) # 过滤条件
    ordering = ("-id",)  # 降序 排序
    # fields = ("name", "address") # 编辑字段
    exclude = ("name", "address") # 不需要编辑的字段

admin.site.register(Author)
admin.site.register(AuthorDetail)
# admin.site.register(Publisher, PublisherAdmin) # 一种方法
admin.site.register(Book)