from django.urls import path
from .views import search_results, travel_list, book_travel, my_bookings, cancel_booking


app_name = 'bookings'

urlpatterns = [
    path("search/", search_results, name="search_results"),
    path("travels/", travel_list, name="travel_list"),
    path("book/<int:travel_id>/", book_travel, name="book_travel"),
    path("my-bookings/", my_bookings, name="my_bookings"),
    path("cancel/<int:booking_id>/", cancel_booking, name="cancel_booking"),
]
