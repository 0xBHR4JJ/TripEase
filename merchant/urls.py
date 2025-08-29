from django.urls import path
from . import views

app_name = "merchant"

urlpatterns = [
    path("login/", views.merchant_login_view, name="login"),
    path("logout/", views.merchant_logout_view, name="logout"),
    path("home/", views.merchant_home_view, name="home"),
    path('signup/',views.merchant_signup_view,name='signup'),
]
