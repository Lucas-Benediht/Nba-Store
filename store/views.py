from django.shortcuts import render, redirect
from . models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # Usado para criar usuários
from .forms import SignUpForm
from django import forms


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




