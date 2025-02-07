from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import datetime
from  ecommerce.models import Product




class ShippingAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255,null=True,blank=True)
    shipping_zipcode = models.CharField(max_length=255,null=True,blank=True)
    shipping_country = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Shipping Address"

        def __str__(self) :
            return f"Shipping address  {str(self.id)}"
        
        
def create_shipping(sender,instance,created,**kwargs):
    if created:
        shipping_address = ShippingAddress(user=instance)
        shipping_address.save()

post_save.connect(create_shipping,sender=User)



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=250)
    shipping_address = models.TextField(max_length=20000)
    amount_paid = models.DecimalField(decimal_places=2,max_digits=10)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"order {str(self.id)}"
    
# auto add shipping date 

@receiver(pre_save,sender=Order)
def set_shipped_date(sender,instance,**kwargs):
    if instance.pk:
        now = datetime.datetime.now()
        obj = sender._default_manager.get(pk=instance.pk)
        if instance.shipped and not obj.shipped:
            instance.date_shipped = now
            
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveBigIntegerField(default=
                                              1)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"order Item {str(self.id)}"
    


