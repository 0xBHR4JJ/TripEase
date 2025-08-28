# from django.db import models
# from django.conf import settings
# from merchant.models import Bus

# class TravelOption(models.Model):
#     TYPE_CHOICES = (
#         ("Flight", "Flight"),
#         ("Train", "Train"),
#         ("Bus", "Bus"),
#     )

#     bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="travel_options", null=True, blank=True)
#     type = models.CharField(max_length=10, choices=TYPE_CHOICES)
#     source = models.CharField(max_length=100)
#     destination = models.CharField(max_length=100)
#     date_time = models.DateTimeField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available_seats = models.PositiveIntegerField()

#     def __str__(self):
#         if self.type == "Bus" and self.bus:
#             return f"{self.bus.bus_number} from {self.source} to {self.destination}"
#         return f"{self.type} from {self.source} to {self.destination}"

#     @classmethod
#     def search(cls, travel_type, source, destination, date):
#         """Return available travel options matching search criteria."""
#         return cls.objects.filter(
#             type=travel_type,
#             source__iexact=source,
#             destination__iexact=destination,
#             date_time__date=date,
#             available_seats__gt=0
#         )


# class Booking(models.Model):
#     STATUS_CHOICES = (
#         ("Confirmed", "Confirmed"),
#         ("Cancelled", "Cancelled"),
#     )

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
#     travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE, related_name="bookings")
#     seats = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Confirmed")

#     def save(self, *args, **kwargs):
#         if self.seats and self.travel_option:
#             if self.travel_option.available_seats < self.seats:
#                 raise ValueError("Not enough available seats")
#             self.total_price = self.seats * self.travel_option.price
#             self.travel_option.available_seats -= self.seats
#             self.travel_option.save()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Booking {self.id} by {self.user.username}"


# bookings/models.py
from django.db import models
from django.conf import settings
from transport.models import TravelOption  # ✅ import from transport

class Booking(models.Model):
    STATUS_CHOICES = (
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE, related_name="bookings")
    seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Confirmed")

    def save(self, *args, **kwargs):
        if self.seats and self.travel_option:
            if self.travel_option.available_seats < self.seats:
                raise ValueError("Not enough available seats")
            self.total_price = self.seats * self.travel_option.price
            self.travel_option.available_seats -= self.seats
            self.travel_option.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
