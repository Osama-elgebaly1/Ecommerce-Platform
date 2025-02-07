from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    # auth system
    path('register/',views.register,name='register'),
    path('login/',views.log,name='login'),
    path('logout/',views.out,name='logout'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:name>',views.category,name='category'),
    path('update_user/',views.update_user,name='update_user'),
    path('update_info/',views.update_info,name='update_info'),
    path('update_password/',views.update_password,name='update_password'),
    path('search/',views.search,name='search'),
   
]
