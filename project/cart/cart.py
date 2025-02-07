from ecommerce.models import Product,Profile

class Cart():
    def __init__(self,request):
        self.session = request.session
        self.request = request

        # if new user , there is no  session key , let's create one
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}

        cart = self.session.get('session_key')

        self.cart = cart

    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product.id in self.cart:
            pass

        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True
        if self.request.user.is_authenticated:
            profile = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            profile.update(old_cart=carty)



    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        # get ids from cart 
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids) 
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def total(self):
        cart = self.cart
        products_ids = cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        total = 0
        for key , value in cart.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.price_after_dis > 0 and product.price != product.price_after_dis:
                        total = total + (product.price_after_dis * value)
                    else:
                        total = total + (product.price * value)
               

        return total
                



    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
        cart = self.cart
        cart[product_id] = product_qty
        self.session.modified = True
        if self.request.user.is_authenticated:
            profile = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            profile.update(old_cart=carty)

        return cart
    def delete(self,product):
        product = str(product)
        cart = self.cart
        del cart[product]
        self.session.modified = True
        if self.request.user.is_authenticated:
            profile = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            profile.update(old_cart=carty)
        return cart


        
        


