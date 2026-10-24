from django.urls import path
from . import views

app_name = "vehicules"

urlpatterns = [
    path("", views.cars, name="liste_vehicules"),
    path("<int:pk>/", views.detail_vehicule, name="detail_vehicule"),
    path("cars/<int:id>/", views.car_single, name="car_single"),
    path("booking_test/", views.booking, name="booking_test"),
    path("about_test/", views.about, name="about_test"),
    path("contact_test/", views.contact, name="contact_test"),
]