from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import Order

# Create your views here.
def index(request):
    return render(request, 'base/home.html')

# Rendering Orders
def home(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'base/home.html', context)

#Creating Order Form
@login_required
def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()

            return redirect('base-home')
    else: 
        form = OrderForm()
    return render(request, 'base/order.html', {'form': form})
