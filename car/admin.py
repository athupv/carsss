from django.contrib import admin
from .models import Car

# class CarAdmin(admin.ModelAdmin):
#     verbose_name_plural = 'Car Data'

admin.site.register(Car)