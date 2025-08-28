# bookings/models.py
from django.db import models
from django.conf import settings
from transport.models import TravelOption  

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


@property
def seats_left(self):
    confirmed = self.bookings.filter(status="Confirmed")
    booked = sum(b.seats for b in confirmed)
    return self.total_seats - booked
