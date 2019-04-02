from django.db import models


class User_Detail(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	utype=models.CharField(max_length=10)
	#phone=models.BigIntegerField()
	phone=models.BigIntegerField(null=True)
	email=models.CharField(max_length=50)
	active=models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	pin=models.IntegerField()
	#userimg=models.ImageField(max_length=100,null=True)
	userimage=models.CharField(max_length=100,null=True)
	address=models.CharField(max_length=150)
	
	def __str__(self):
		return self.username

class Category(models.Model):
	categoryname=models.CharField(max_length=100)
	active=models.CharField(max_length=50)	
	def __str__(self):
		return self.categoryname
	
class Product(models.Model):
	pcategoryid=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE,)
	pname=models.CharField(max_length=50)
	pdescription=models.CharField(max_length=150)
	pimg=models.CharField(max_length=100,null=True)
	pquantity=models.FloatField()
	pprice=models.FloatField()
	uploaded_date=models.DateTimeField(auto_now_add=True)
	user_detailid=models.ForeignKey(User_Detail,related_name='product',on_delete=models.CASCADE,)
	active=models.CharField(max_length=50)	
	
	def __str__(self):
		return self.pname
class Purchase(models.Model):
	pid=models.ForeignKey(Product,related_name='purchase',on_delete=models.CASCADE,)
	purchase_date=models.DateTimeField(auto_now_add=True)
	purchaseprice=models.FloatField()
	tax=models.FloatField()
	Tcost=models.FloatField()
	purchaseuid=models.ForeignKey(User_Detail,related_name='purchase',on_delete=models.CASCADE,)
	pquantity=models.FloatField()
	
	
	
"""	
class Topic(models.Model):
	subject=models.CharField(max_length=255)
	last_updated=models.DateTimeField(auto_now_add=True)
	board=models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE,)
	starter=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE,)

class Post(models.Model):
	message=models.TextField(max_length=4000)
	topic=models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE,)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateField(null=True)
	created_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,)
	updated_by=models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE,)
"""

# Create your models here.
