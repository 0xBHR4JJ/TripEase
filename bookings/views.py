from django.shortcuts import render, redirect, get_object_or_404
from .models import TravelOption, Booking
from django.contrib.auth.decorators import login_required


def travel_list(request):
    travels = TravelOption.objects.all()
    return render(request, "travel_list.html", {"travels": travels})

@login_required(login_url="accounts:login")

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
            return redirect("bookings:my_bookings")
    return render(request, "booking_form.html", {"travel": travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)

    # only confirmed bookings for totals
    confirmed = bookings.filter(status="Confirmed")

    total_seats = sum(b.seats for b in confirmed)
    total_price = sum(b.total_price for b in confirmed)

    return render(request, "my_bookings.html", {
        "bookings": bookings,        
        "total_seats": total_seats,  
        "total_price": total_price, 
    })



@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = "Cancelled"
    booking.travel_option.available_seats += booking.seats
    booking.travel_option.save()
    booking.save()
    return redirect("bookings:my_bookings")



from datetime import datetime, timedelta

def search_results(request):
    results = []
    travel_type = source = destination = date = None
    prev_date = next_date = None

    if request.GET:  # triggered on form submission
        travel_type = request.GET.get("type")
        source = request.GET.get("source")
        destination = request.GET.get("destination")
        date = request.GET.get("date")

    # inside search_results
    if travel_type and source and destination and date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
            prev_date = (parsed_date - timedelta(days=1)).strftime("%Y-%m-%d")
            next_date = (parsed_date + timedelta(days=1)).strftime("%Y-%m-%d")

            # Pass string, not date object
            results = TravelOption.search(travel_type, source, destination, date)
        except ValueError:
            results = []


    context = {
        "results": results,
        "travel_type": travel_type,
        "source": source,
        "destination": destination,
        "date": date,
        "prev_date": prev_date,
        "next_date": next_date,
    }
    return render(request, "search_results.html", context)
