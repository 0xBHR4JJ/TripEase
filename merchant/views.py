from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MerchantLoginForm
from .models import Bus
from .forms import MerchantSignupForm
from .decorators import merchant_required
from django.contrib.auth.decorators import login_required

def merchant_signup_view(request):
    if request.method == "POST":
        form = MerchantSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("merchant:home")
    else:
        form = MerchantSignupForm()
    return render(request, "merchant_signup.html", {"form": form})

@login_required(login_url="merchant:login")
@merchant_required
def add_travel_option(request):
    merchant = request.user.merchantprofile
    if request.method == "POST":
        form = TravelOptionForm(request.POST, merchant=merchant)
        if form.is_valid():
            travel_option = form.save(commit=False)
            travel_option.merchant = merchant
            travel_option.save()
            return redirect("merchant:traveloption_list")
    else:
        form = TravelOptionForm(merchant=merchant)
    return render(request, "transport/traveloption_form.html", {"form": form})


# @login_required(login_url="merchant:login")
# @merchant_required
# def dashboard_view(request):
#     merchant = request.user.merchantprofile

#     # Key metrics
#     bus_count = Bus.objects.filter(merchant=merchant).count()
#     option_qs = TravelOption.objects.filter(merchant=merchant)
#     option_count = option_qs.count()

#     # If your Booking model references transport.TravelOption, this works:
#     booking_qs = Booking.objects.filter(travel_option__merchant=merchant)
#     booking_count = booking_qs.count()

#     # Recents
#     recent_buses = Bus.objects.filter(merchant=merchant).order_by("-id")[:5]
#     recent_options = option_qs.select_related("bus").order_by("-id")[:8]
#     recent_bookings = booking_qs.select_related("travel_option", "user").order_by("-id")[:8]

#     context = {
#         "bus_count": bus_count,
#         "option_count": option_count,
#         "booking_count": booking_count,
#         "recent_buses": recent_buses,
#         "recent_options": recent_options,
#         "recent_bookings": recent_bookings,
#     }
#     return render(request, "merchant_dashboard.html", context)


# def merchant_login_view(request):
#     if request.method == "POST":
#         form = MerchantLoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user is not None and user.role == "merchant":
#                 login(request, user)
#                 return redirect("merchant:home")
#             else:
#                 form.add_error(None, "Invalid credentials or not a merchant account.")
#     else:
#         form = MerchantLoginForm()
#     return render(request, "merchant_login.html", {"form": form})


def merchant_login_view(request):
    if request.method == "POST":
        form = MerchantLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None and user.role == "merchant":
                login(request, user)
                return redirect("merchant:home")
            else:
                form.add_error(None, "Invalid credentials or not a merchant account.")
    else:
        form = MerchantLoginForm()
    return render(request, "merchant_login.html", {"form": form})


def merchant_logout_view(request):
    logout(request)
    return redirect("merchant:login")


def merchant_home_view(request):
    return render(request, "merchant_home.html")
