from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("merchant", "Merchant"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="customer")

    def __str__(self):
        return self.username
