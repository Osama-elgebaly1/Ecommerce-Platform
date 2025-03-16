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
'''    
    Adds a product to the shopping cart.

    This view handles AJAX POST requests to add a product to the session-based cart. 
    It retrieves the product and quantity from the request, updates the cart, 
    and returns a JSON response with the updated cart quantity.

    Expected POST data:
        - action (str): Should be 'post' to trigger the add operation.
        - product_id (int): The ID of the product to add.
        - product_qty (int): The quantity of the product to add.

    Returns:
        JsonResponse: A response containing the updated cart quantity.
   
'''
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
"""
    Updates the quantity of a product in the shopping cart.

    This view handles AJAX POST requests to modify the quantity of an 
    existing product in the session-based cart.

    Expected POST data:
        - action (str): Should be 'post' to trigger the update operation.
        - product_id (int): The ID of the product to update.
        - product_qty (int): The new quantity of the product.

    Returns:
        JsonResponse: A response containing the updated quantity.
    """
	cart = Cart(request)
	if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            cart.update(product=product_id, quantity=product_qty)
            messages.success(request,"Product is updated succesfully...")
            response = JsonResponse({'qty':product_qty})
            return response


    




def cart_delete(request):
"""
    Removes a product from the shopping cart.

    This view handles AJAX POST requests to delete a product from 
    the session-based cart.

    Expected POST data:
        - action (str): Should be 'post' to trigger the delete operation.
        - product_id (int): The ID of the product to remove.

    Returns:
        JsonResponse: A response confirming the deleted product ID.
    """
        cart = Cart(request)
        if request.POST.get('action') == 'post':
              product_id = int(request.POST.get('product_id'))
              cart.delete(product=product_id)
              messages.success(request,"Product is deleted succesfully...")
              response = JsonResponse({'product':product_id})
              messages.success(request,'Product is deleted succesfully...')
              return response
                  
    


