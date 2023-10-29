from django.shortcuts import render, redirect, get_object_or_404
from . models import Product, Category, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # Usado para criar usuários
from .forms import SignUpForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum


def category(request, foo):
	# Replace Hyphens with Spaces
	foo = foo.replace('-', ' ')
	# Grab the category from the url
	try:
		# Look Up The Category
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'category.html', {'products':products, 'category':category})
	except:
		messages.success(request, ("That Category Doesn't Exist..."))
		return redirect('home')
    

def product(request, pk):
    product = Product.objects.get(id=pk) # Pegando as caracteristicas
    return render(request, 'product.html', {'product': product})

def home(request):
    # Importar as caractersticas do produto para aparecer no html
    products = Product.objects.all() # Pegando as caracteristicas
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST": #Verificando o método enviado pelo form no html
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password) # Verificando a autenticação de usuário e senha
        if user is not None: 
            login(request, user)
            messages.success(request, "Login Realizado com sucesso!")
            return redirect('home')
            
            
        else:
            messages.error(request, "Username ou senha incorreto! Tente novamente")
            return redirect ('login')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout Realizado com Sucesso!")
    return redirect ('login')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You Have Registered Successfully!! Welcome!"))
            return redirect('home')
        else:
            messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})


def all_product(request):
    products = Product.objects.all() # Pegando as caracteristicas
    return render(request, 'all_product.html', {'products': products})

from django.db.models import Sum

@login_required
def shopcart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    # Calculate the total cart price
    cart_total = cart_items.annotate(
        total_price=F('product__price') * F('quantity')
    ).aggregate(total=Sum('total_price'))['total']

    # Calculate the total number of items in the cart
    cart_count = cart_items.aggregate(total_count=Sum('quantity'))['total_count']

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart_count': cart_count,  # Add the cart count to the context
    }

    return render(request, 'shopcart.html', context)



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Verifique se o item já está no carrinho do usuário
    existing_item = CartItem.objects.filter(user=user, product=product).first()

    if existing_item:
        # Se o item já está no carrinho, aumente a quantidade
        existing_item.quantity += 1
        existing_item.save()
    else:
        # Caso contrário, crie um novo item no carrinho
        new_item = CartItem(user=user, product=product, quantity=1)
        new_item.save()

    return redirect('shopcart')

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Verifique se o item está no carrinho do usuário
    existing_item = CartItem.objects.filter(user=user, product=product).first()

    if existing_item:
        if existing_item.quantity > 1:
            # Se houver mais de um item, diminua a quantidade
            existing_item.quantity -= 1
            existing_item.save()
        else:
            # Caso contrário, remova o item do carrinho
            existing_item.delete()

    return redirect('shopcart')

def update_cart_total(user):
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.total_price for item in cart_items)
    user.cart.total_price = total_price
    user.cart.save()
    
