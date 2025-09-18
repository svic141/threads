from django.shortcuts import render, redirect, get_object_or_404

from item.models import Category, Item
from .forms import SignupForm, LoginForm, EditUserForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    items =Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {'categories':categories, 'items':items, })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else:
        form =  SignupForm()

    return render(request, 'core/signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/index')
        
    else:
        form =  LoginForm()

    return render(request, 'core/login.html', {'form':form})

def editUser(request, pk):
    user = get_object_or_404(User, pk=pk, username=request.username)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('dashboard:index', pk=user.id)
    else:
        form = EditUserForm(instance=user)
    
    return render(request, 'core/edit.html', {'form':form, 'title': 'Edit Details'})