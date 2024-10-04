from django.shortcuts import render,redirect
from .forms import CarForm
from .models import Car
from django.contrib import messages


def home(request):
    return render(request, 'home.html') 

def top_selling_car(request):
    cars = Car.objects.order_by('-selling_quantity')[:1]
    return render(request, 'top_selling_car.html', {'cars': cars})

def top_rated_car(request):
    cars = Car.objects.order_by('-rating')[:1] 
    return render(request, 'top_rated_car.html', {'cars': cars})

def oldest_car(request):
    cars = Car.objects.order_by('manufacturing_year')[:1]
    return render(request, 'oldest_car.html', {'cars': cars})


def newest_car(request):
    cars = Car.objects.order_by('-manufacturing_year')[:1]
    return render(request, 'newest_car.html', {'cars': cars})

def all_cars(request):
    cars = Car.objects.all()
    return render(request, 'all_cars.html', {'cars': cars})






def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully.')  # Add a success message
            return redirect('add_car ')  # Redirect to a page displaying the list of cars
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})



    



