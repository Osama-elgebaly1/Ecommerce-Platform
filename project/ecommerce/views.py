from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Product,Category,Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login,logout
from django.contrib import messages
from .forms import SignUpForm,LoginForm,UpdateUserForm,ChangePasswordForm,UserInfoForm
from django.db.models import Q
import  json
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
# Create your views here.

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__icontains = searched) | Q(description__icontains = searched))
        if not products:
            messages.success(request,'This product is not exist...Please try again')
        return render(request,'pages/search.html',{'products':products})
    else:
        return render(request,'pages/search.html',{})




def update_info(request):
    if request.user.is_authenticated:
        current_user  = ShippingAddress.objects.get(user_id = request.user.id)
        shipping_form = ShippingForm(request.POST or None ,instance=current_user)

        current_profile = Profile.objects.get(user_id = request.user.id)
        form = UserInfoForm(request.POST or None , instance=current_profile)
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request,'Your info has been updated....')
            return redirect('home')
        else:
            return render(request,'pages/update_info.html',{'form':form,'shipping_form':shipping_form})
    else:
        messages.success(request,'You must be logged in to access this page...')
        return redirect('login')
    
    

def update_password(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(user , request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Your password has been updated...')
                login(request,user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(user)
            return render(request,'pages/update_password.html',{'form':form})
    else:
        messages.success(request,'You must be logged in to access that page...')
        return redirect('login')


def update_user(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None , instance = user)
        if form.is_valid():
            form.save()
            messages.success(request,'Your info have been updated...')
            login(request,user)
            return redirect('home')
        
        
        return render(request,'pages/update_user.html',{'form':form})
    else:
        messages.success(request,'You must be logged in to access that page ...')
        return redirect('login')
    

def home(request):
    products = Product.objects.all()
    return render(request,'pages/index.html',{'products':products,
                                              })

def about(request):
    return render(request,'pages/about.html')


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in
            user = authenticate(username=username,password=password)
            login(request,user=user)
            messages.success(request,'Congratulations , You have been registered.... ')
            return redirect('home')
        else:
            messages.success(request,'Whoops , there was a problem registering  , please try again ...')
            return redirect('register')
    else:
        return render(request,'pages/register.html',{'form':form})
    



def log(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                profile = Profile.objects.get(user__id = request.user.id)
                old_cart = profile.old_cart
                if old_cart:
                    converted_cart = json.loads(old_cart)
                    for key,value in converted_cart.items():
                        cart = Cart(request)
                        product = Product.objects.get(id=key)
                        cart.add(product=product,quantity=value)
                        


                messages.success(request,'You have been logged in ...')
                return redirect('home')

            







            else:
                messages.success(request,'User is not exist , please create an account...')
                return redirect('register')
            
        else:
            messages.success(request,'User name or password is incorrect...')
            return redirect('login')
    else:
        return render(request,'pages/login.html',{'form':form})
            





def out(request):
    logout(request)
    messages.success(request,"Logged out....")
    return redirect('home')



def product(request,pk):
    product = Product.objects.get(id=pk)
    related_products = Product.objects.filter(category=product.category)[:3]
    return render(request,'pages/product.html',{'product':product,
                                                'products':related_products,
                                                })


def category(request,name):
    category = Category.objects.get(name=name)
    products = Product.objects.filter(category=category)
    return render(request,'pages/index.html',{'products':products,
                                              })