from django.db import models

# Create your models here.
from django.db import models
from merchant.models import Bus, MerchantProfile

class TravelOption(models.Model):
    TYPE_CHOICES = (
        ("Flight", "Flight"),
        ("Train", "Train"),
        ("Bus", "Bus"),
    )

    merchant = models.ForeignKey(
        MerchantProfile, on_delete=models.CASCADE, related_name="travel_options"
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    bus = models.ForeignKey(
        Bus, on_delete=models.CASCADE, related_name="travel_options", null=True, blank=True
    )
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    repeat_days = models.CharField(max_length=50, blank=True, null=True)

    # Optional flight/train fields
    flight_number = models.CharField(max_length=50, blank=True, null=True)
    airline = models.CharField(max_length=100, blank=True, null=True)
    duration_minutes = models.PositiveIntegerField(blank=True, null=True)  # for flight/train
    train_number = models.CharField(max_length=50, blank=True, null=True)
    coach_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.type == "Bus" and self.bus:
            return f"{self.bus.bus_number} from {self.source} to {self.destination}"
        return f"{self.type} from {self.source} to {self.destination}"

    @classmethod
    def search(cls, travel_type, source, destination, date):
        return cls.objects.filter(
            type=travel_type,
            source__iexact=source,
            destination__iexact=destination,
            date_time__date=date,
            available_seats__gt=0
        )
