from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import ShippingForm,ShippingAddress,PaymentForm
from django.contrib import messages
from .models import Order , OrderItem
import datetime
from ecommerce.models import Profile
# Create your views here.

def payment_success(request):
    return render(request,'payment/payment_success.html',{})

def checkout(request):
    cart = Cart(request)
    products = cart.get_prods
    quantities = cart.get_quants
    total = cart.total()
    if request.user.is_authenticated:
        current_user  = ShippingAddress.objects.get(user_id = request.user.id)
        shipping_form = ShippingForm(request.POST or None ,instance=current_user)
    else:
        shipping_form = ShippingForm(request.POST or None)

        

    return render(request,'payment/checkout.html',{
                                       'products':products,
                                       'quantities':quantities,
                                       'total':total,
                                       'shipping_form':shipping_form})






def billing_info(request):
        if request.POST:
            cart = Cart(request)
            products = cart.get_prods
            quantities = cart.get_quants
            total = cart.total()
            shipping_form = request.POST
            request.session['shipping_info'] = shipping_form
            if request.user.is_authenticated:
                billing_form = PaymentForm()


                return render(request,'payment/billing_info.html',{
                                                'products':products,
                                                'quantities':quantities,
                                                'total':total,
                                                'shipping_info':shipping_form,
                                                'billing_form':billing_form
                                                })
            

            else:
                billing_form = PaymentForm()
                return render(request,'payment/billing_info.html',{
                                                'products':products,
                                                'quantities':quantities,
                                                'total':total,
                                                'shipping_info':shipping_form,
                                                'billing_form':billing_form

                                                })
                 
            
                 
        else:
             messages.success(request,'Access Denied ')
             return redirect('home')


def order_success(request):
     if request.POST:
        #   importing cart to get total 
          cart = Cart(request)
          products = cart.get_prods
          quantities = cart.get_quants
          total = cart.total()
        
          

          shipping_info = request.session.get('shipping_info')
          full_name = shipping_info.get('shipping_full_name')
          email = shipping_info.get('shipping_email')

          if request.user.is_authenticated:
               user = request.user
          else:
               user = None
               

        ############## address ########

          address1 = shipping_info.get('shipping_address1')
          address2 = shipping_info.get('shipping_address2')
          city = shipping_info.get('shipping_city')
          state = shipping_info.get('shipping_state')
          country = shipping_info.get('shipping_country')
          full_address = f"{address1} \n {address2} \n {city} \n {state} \n {country} "
        
        #   amount_paid = total
          amount_paid = total

        # creating Order 
          order = Order(user = user ,
                        full_name=full_name,
                        email = email,
                        shipping_address = full_address,
                        amount_paid=amount_paid,
                        )
          order.save()

          # creating order items
          order_id  = order.pk
          for product in products():
              product_id = product.id
              user= user
              if product.price != product.price_after_dis and product.price_after_dis > 0:
                    price = product.price_after_dis
              else:
                    price = product.price

              for key,value in quantities().items():
                   if product.id == int(key):
                        quantity = value
                        order_item = OrderItem(
                                          order_id = order_id,
                                          product_id=product_id,
                                          user=user,
                                          price=price,
                                          quantity=quantity)
                        order_item.save()

            # Delete cart 
              for key in list(request.session.keys()):
                   if key == 'session_key':
                        del request.session[key]
          user = Profile.objects.filter(user__id = request.user.id)
          user.update(old_cart="")

          messages.success(request,'Order Placed...')
          return redirect('home')
     else:
          messages.success(request,'Access Denied ')
          return redirect('home')
     

def shipped_dash(request):
     if request.user.is_authenticated and request.user.is_superuser:
          orders = Order.objects.filter(shipped=True)
          if request.method == 'POST':
               status = False
               num = request.POST['num']
               order = Order.objects.filter(id=num)
               order.update(shipped=status)
               messages.success(request,'Status Updated ')


          return render(request,'payment/shipped_dash.html',{'orders':orders})
     else:
          messages.success(request,'Access Denied ')
          return redirect('home')
     
     


def not_shipped_dash(request):
     if request.user.is_authenticated and request.user.is_superuser:
          orders = Order.objects.filter(shipped=False)
          if request.method == 'POST':
               status = True
               num = request.POST['num']
               order = Order.objects.filter(id=num)
               now = datetime.datetime.now()
               order.update(shipped=status,date_shipped=now)
               messages.success(request,'Status Updated ')

          return render(request,'payment/not_shipped_dash.html',{'orders':orders})
     else:
          messages.success(request,'Access Denied ')
          return redirect('home')
     

def orders(request,pk):
      if request.user.is_authenticated and request.user.is_superuser:
          order = Order.objects.get(id=pk)
          items = OrderItem.objects.filter(order = pk)
          if request.method == 'POST':
               status = request.POST['status']
               if status == 'True':
                    order = Order.objects.filter(id=pk)
                    now = datetime.datetime.now()
                    order.update(shipped=True,date_shipped=now)
               else:
                    order = Order.objects.filter(id=pk)
                    order.update(shipped=False)
               messages.success(request,'Order updated ')
               return redirect('home')
          


          return render(request,'payment/orders.html',{'order':order,
                                                       'items':items})
      else:
          messages.success(request,'Access Denied ')
          return redirect('home')
     