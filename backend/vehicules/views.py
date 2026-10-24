from .models import Vehicule
from datetime import timedelta

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from reservations.forms import ReservationForm
from reservations.models import Reservation



def liste_vehicules(request):
    vehicules = Vehicule.objects.filter(disponible=True).order_by("-date_creation")

    return render(
        request,
        "vehicules/liste_vehicule.html",
        {"vehicules": vehicules},
    )


def detail_vehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)

    return render(
        request,
        "vehicules/detail_vehicule.html",
        {"vehicule": vehicule},
    )
from django.shortcuts import render

def cars(request):
    vehicules = Vehicule.objects.filter(disponible=True).order_by("-date_creation")

    return render(
        request,
        "rentaly/car.html",
        {
            "vehicules": vehicules,
        },
    )

def car_single(request, id):

    vehicule = get_object_or_404(Vehicule, pk=id)

    if request.method == "POST":

        form = ReservationForm(request.POST)

        if form.is_valid():

            reservation = form.save(commit=False)

            reservation.vehicule = vehicule

            # Calcul du nombre de jours
            nb_jours = (
                reservation.date_retour - reservation.date_depart
            ).days

            if nb_jours < 1:
                nb_jours = 1

            reservation.montant = nb_jours * vehicule.prix_par_jour

            reservation.save()

            messages.success(
                request,
                "Votre réservation a été enregistrée avec succès."
            )

            return redirect("car_single", id=vehicule.id)

    else:

        form = ReservationForm()

    return render(
        request,
        "rentaly/car-single.html",
        {
            "vehicule": vehicule,
            "form": form,
        },
    )

def booking(request):
    return render(request, "rentaly/booking.html")

def about(request):
    return render(request, "rentaly/about.html")

def contact(request):
    return render(request, "rentaly/contact.html")
    