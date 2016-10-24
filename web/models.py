#coding:utf-8
from django.db import models
from DjangoUeditor.models import UEditorField
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class UserType(models.Model):
	display = models.CharField(max_length=50)
	def __unicode__(self):
		return self.display

class Admin(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField()
	user_type = models.ForeignKey('UserType')
	def __unicode__(self):
		return self.username

class NewsType(models.Model):
	display = models.CharField(max_length=50)
	def __unicode__(self):
		return self.display

class News(models.Model):
	title = models.CharField(max_length=50)
	summary = models.CharField(max_length=400,default="")
	content = models.TextField(max_length=1000,default="")
	url = models.CharField(max_length=100,default="")
	favor_count = models.IntegerField(default=0)
	reply_count = models.IntegerField(default=0)
	news_type = models.ForeignKey('NewsType')
	users = models.ForeignKey('Admin')
	create_date = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.title

class Reply(models.Model):
	users = models.ForeignKey('Admin')
	new = models.ForeignKey('News')
	content = models.CharField(max_length=50)
	create_date = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.content

class Chat(models.Model):
	content = models.TextField()
	user = models.ForeignKey('Admin')
	create_date = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.content

@python_2_unicode_compatible
class Goods(models.Model):
	name = models.CharField(max_length=20)
	value = models.FloatField()
	descript = models.CharField(max_length=254)
	details = models.TextField()
	goodsImg = models.FileField(upload_to = 'static/upload')
	user = models.ForeignKey('Admin')
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Orders(models.Model):
	goods = models.ForeignKey("Goods")
	buyer = models.ForeignKey('Admin',related_name="buyer")
#	sales = models.ForeignKey('Admin',related_name="sales")
	create_date = models.DateTimeField(auto_now_add = True)
	reciever = models.CharField(max_length=54,default="")
	address = models.CharField(max_length=254,default="")
	phone = models.IntegerField(max_length=20,default=0)
#	pay = models.FloatField(default=0.0)
	def __str__(self):
		return self.reciever