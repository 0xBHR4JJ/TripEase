from django.shortcuts import render

# Create your views here.

# create a default home view 
def home_view(request):
    context = {"title": "TripEase"}
    return render(request,"home.html") 
