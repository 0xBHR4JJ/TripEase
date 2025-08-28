from django.shortcuts import render, redirect, get_object_or_404
from .models import TravelOption, Booking
from django.contrib.auth.decorators import login_required

def travel_list(request):
    travels = TravelOption.objects.all()
    return render(request, "travel_list.html", {"travels": travels})

@login_required
def book_travel(request, travel_id):
    travel = get_object_or_404(TravelOption, id=travel_id)
    if request.method == "POST":
        seats = int(request.POST["seats"])
        if seats <= travel.available_seats:
            total_price = seats * travel.price
            Booking.objects.create(user=request.user, travel_option=travel,
                                   seats=seats, total_price=total_price)
            travel.available_seats -= seats
            travel.save()
            return redirect("my_bookings")
    return render(request, "booking_form.html", {"travel": travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "my_bookings.html", {"bookings": bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = "Cancelled"
    booking.travel_option.available_seats += booking.seats
    booking.travel_option.save()
    booking.save()
    return redirect("my_bookings")
