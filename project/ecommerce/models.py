from django.db import models
import datetime 
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20,blank=True)
    address1 = models.CharField(max_length=200,blank=True)
    address2 = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200,blank=True)
    state = models.CharField(max_length=200,blank=True)
    zipcode = models.CharField(max_length=200,blank=True)
    country = models.CharField(max_length=200,blank=True)
    old_cart= models.CharField(max_length=1000,blank=True,null=True)
    def __str__(self):
        return self.user.username


def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# sending a signal ( post_save ) to the receiver ( create_profile ) when the user is saved 
post_save.connect(create_profile,sender=User)

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    price_after_dis = models.DecimalField(max_digits=6,decimal_places=2,default=0)
    description = models.TextField(max_length=250,default='',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    def __str__(self) -> str:
        return self.name




class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name
    

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    address = models.CharField(max_length=200,)
    phone = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self) :
        return self.product