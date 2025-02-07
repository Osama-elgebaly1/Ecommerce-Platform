from django.shortcuts import render , get_object_or_404,redirect
from ecommerce.models import Category
from .cart import Cart
from ecommerce.models import Product
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def summary(request):
    cart = Cart(request)
    products = cart.get_prods
    quantities = cart.get_quants
    total = cart.total()
    return render(request,'cart.html',{
                                       'products':products,
                                       'quantities':quantities,
                                       'total':total})





def add(request):
    # Get the cart
    cart = Cart(request)
    #  test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product,quantity=product_qty)
        # get cart qty
        cart_quantity = cart.__len__()
        # return response 
        # response = JsonResponse({'product name :':product.name})
        response = JsonResponse({'qty':cart_quantity})
        messages.success(request,"Product is added succesfully....")
        return response

    



def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            cart.update(product=product_id, quantity=product_qty)
            messages.success(request,"Product is updated succesfully...")
            response = JsonResponse({'qty':product_qty})
            return response


    




def cart_delete(request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
              product_id = int(request.POST.get('product_id'))
              cart.delete(product=product_id)
              messages.success(request,"Product is deleted succesfully...")
              response = JsonResponse({'product':product_id})
              messages.success(request,'Product is deleted succesfully...')
              return response
                  
    


