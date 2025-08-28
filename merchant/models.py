from django.db import models
from django.conf import settings
from django import forms


class MerchantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Business information
    company_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    business_address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    # Contact information
    contact_person_name = models.CharField(max_length=100, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)

    # Bank / payout info
    bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_ifsc = models.CharField(max_length=20, blank=True, null=True)

    # Optional branding / analytics
    logo = models.ImageField(upload_to="merchant_logos/", blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.company_name


class Bus(models.Model):
    merchant = models.ForeignKey(MerchantProfile, on_delete=models.CASCADE, related_name="buses")
    bus_number = models.CharField(max_length=50)
    total_seats = models.PositiveIntegerField()
    model_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.bus_number} - {self.merchant.company_name}"


# class TravelOptionForm(forms.ModelForm):
#     class Meta:
#         model = TravelOption
#         fields = ["type", "bus", "source", "destination", "date_time", "price", "available_seats"]

#     def __init__(self, *args, **kwargs):
#         merchant = kwargs.pop("merchant", None)
#         super().__init__(*args, **kwargs)
#         if merchant:
#             self.fields["bus"].queryset = merchant.buses.all()
