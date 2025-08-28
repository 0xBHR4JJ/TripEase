from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TravelOptionForm, BusForm
from .models import TravelOption
from merchant.models import MerchantProfile, Bus

# ---------------- TravelOption CRUD ----------------

@login_required(login_url="merchant:login")
def traveloption_list(request):
    merchant = request.user.merchantprofile
    options = TravelOption.objects.filter(merchant=merchant)
    return render(request, "transport/traveloption_list.html", {"options": options})

@login_required(login_url="merchant:login")
def traveloption_add(request):
    merchant = request.user.merchantprofile
    if request.method == "POST":
        form = TravelOptionForm(request.POST, merchant=merchant)
        if form.is_valid():
            travel_option = form.save(commit=False)
            travel_option.merchant = merchant
            travel_option.save()
            return redirect("transport:traveloption_list")
    else:
        form = TravelOptionForm(merchant=merchant)
    return render(request, "transport/traveloption_form.html", {"form": form})

@login_required(login_url="merchant:login")
def traveloption_edit(request, pk):
    merchant = request.user.merchantprofile
    travel_option = get_object_or_404(TravelOption, pk=pk, merchant=merchant)
    if request.method == "POST":
        form = TravelOptionForm(request.POST, instance=travel_option, merchant=merchant)
        if form.is_valid():
            form.save()
            return redirect("transport:traveloption_list")
    else:
        form = TravelOptionForm(instance=travel_option, merchant=merchant)
    return render(request, "transport/traveloption_form.html", {"form": form})

@login_required(login_url="merchant:login")
def traveloption_delete(request, pk):
    merchant = request.user.merchantprofile
    travel_option = get_object_or_404(TravelOption, pk=pk, merchant=merchant)
    if request.method == "POST":
        travel_option.delete()
        return redirect("transport:traveloption_list")
    return render(request, "transport/traveloption_confirm_delete.html", {"travel_option": travel_option})

# ---------------- Bus CRUD ----------------

@login_required(login_url="merchant:login")
def bus_list(request):
    merchant = request.user.merchantprofile
    buses = Bus.objects.filter(merchant=merchant)
    return render(request, "transport/bus_list.html", {"buses": buses})

@login_required(login_url="merchant:login")
def bus_add(request):
    merchant = request.user.merchantprofile
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            bus = form.save(commit=False)
            bus.merchant = merchant
            bus.save()
            return redirect("transport:bus_list")
    else:
        form = BusForm()
    return render(request, "transport/bus_form.html", {"form": form})

@login_required(login_url="merchant:login")
def bus_edit(request, pk):
    merchant = request.user.merchantprofile
    bus = get_object_or_404(Bus, pk=pk, merchant=merchant)
    if request.method == "POST":
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect("transport:bus_list")
    else:
        form = BusForm(instance=bus)
    return render(request, "transport/bus_form.html", {"form": form})

@login_required(login_url="merchant:login")
def bus_delete(request, pk):
    merchant = request.user.merchantprofile
    bus = get_object_or_404(Bus, pk=pk, merchant=merchant)
    if request.method == "POST":
        bus.delete()
        return redirect("transport:bus_list")
    return render(request, "transport/bus_confirm_delete.html", {"bus": bus})
