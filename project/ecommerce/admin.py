from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your other models first
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Profile)



