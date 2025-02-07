
from .cart import Cart
from ecommerce.models import Category

# create context processor

def cart(request):
    return {'cart':Cart(request)}


def categories(request):
    categories = Category.objects.all()
    return {'categories':categories}