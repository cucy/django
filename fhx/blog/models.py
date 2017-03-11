from django.db import models

# Create your models here.

class Article(models.Model):
	title=models.CharField("标题",max_length=50)
	zhuozhe=models.CharField("作者",max_length=50)
	created_date=models.DateField("创建日期",auto_now_add=True)
	modify_date=models.DateField("修改日期",auto_now=True)
	content=models.TextField()	
	is_show=models.BooleanField()

	class Meta:
		db_table="article"

	def __str__(self):
		return self.title




