"""
URL configuration for TripEase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconffrom django.db import models
from django.contrib.auth.models import User

class TravelOption(models.Model):
    TYPE_CHOICES = (("Flight", "Flight"), ("Train", "Train"), ("Bus", "Bus"))
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.type} from {self.source} to {self.destination}"

class Booking(models.Model):
    STATUS_CHOICES = (("Confirmed", "Confirmed"), ("Cancelled", "Cancelled"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Confirmed")

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('b/',include('bookings.urls')),
    path('a/',include('accounts.urls')),
    path('m/',include('merchant.urls')),
    path('t/',include('transport.urls')),
]
