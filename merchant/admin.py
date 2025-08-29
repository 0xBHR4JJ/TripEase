from django.contrib import admin
from .models import MerchantProfile, Bus

@admin.register(MerchantProfile)
class MerchantProfileAdmin(admin.ModelAdmin):
    list_display = ("company_name", "user", "license_number")

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ("bus_number", "merchant", "total_seats", "model_name")
