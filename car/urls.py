from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('top-selling-car/', views.top_selling_car, name='top_selling_car'),
    path('top-rated-car/', views.top_rated_car, name='top_rated_car'),
    path('oldest-car/', views.oldest_car, name='oldest_car'),
    path('newest-car/', views.newest_car, name='newest_car'),
    path('all-cars/', views.all_cars, name='all_cars'),
    path('add-car/', views.add_car, name='add_car'),
]   