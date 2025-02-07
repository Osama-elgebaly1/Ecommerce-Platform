from django.urls import path
from . import views
urlpatterns = [
    path('payment_success/',views.payment_success,name='payment_success'),
    path('checkout/',views.checkout,name='checkout'),
    path('billing_info/',views.billing_info,name='billing_info'),
    path('order_success/',views.order_success,name='order_success'),
    path('shipped_dash/',views.shipped_dash,name='shipped_dash'),
    path('not_shipped_dath/',views.not_shipped_dash,name='not_shipped_dash'),
    path('Orders/<int:pk>',views.orders,name='orders'),
]
