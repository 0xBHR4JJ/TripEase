from django.urls import path
from . import views

app_name = "transport"

urlpatterns = [
    # TravelOption URLs
    path("travel-options/", views.traveloption_list, name="traveloption_list"),
    path("travel-options/add/", views.traveloption_add, name="traveloption_add"),
    path("travel-options/edit/<int:pk>/", views.traveloption_edit, name="traveloption_edit"),
    path("travel-options/delete/<int:pk>/", views.traveloption_delete, name="traveloption_delete"),

    # Bus URLs
    path("buses/", views.bus_list, name="bus_list"),
    path("buses/add/", views.bus_add, name="bus_add"),
    path("buses/edit/<int:pk>/", views.bus_edit, name="bus_edit"),
    path("buses/delete/<int:pk>/", views.bus_delete, name="bus_delete"),
]
