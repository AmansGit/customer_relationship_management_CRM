from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	# id 				= models.PrimaryKey(autoincrement=True)
	user			= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name			= models.CharField(max_length=200, null=True)
	phone			= models.CharField(max_length=10, null=True)
	email			= models.EmailField(max_length=100, null=True)
	profile_pic		= models.ImageField(null=True)
	date_created	= models.DateTimeField(auto_now_add=True, null=True)	

	def __str__(self):
		return self.name

class Tag(models.Model):
	# id 				= models.PrimaryKey(autoincrement=True)
	name			= models.CharField(max_length=200, null=True)	

	def __str__(self):
		return self.name 

class Product(models.Model):
	CATEGORY		= (
					('Indoor', 'Indoor'),
					('Out Door', 'Out Door'),
		)
	name			= models.CharField(max_length=200, null=True)
	price			= models.FloatField(null=True)
	catagory		= models.CharField(max_length=200, null=True, choices=CATEGORY)
	description		= models.TextField(null=True, blank=True)
	date_created	= models.DateTimeField(auto_now_add=True, null = True, blank=True)
	tags 			= models.ManyToManyField(Tag)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS			= (
					('Pending', 'Pending'),
					('Out for Delivery', 'Out for Delivery'),
					('Delivered', 'Delivered')
		)
	customer 		= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product 		= models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	date_created	= models.DateTimeField(auto_now_add=True, null=True)
	status 			= models.CharField(max_length=200, null=True, choices=STATUS)
	note 			= models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name