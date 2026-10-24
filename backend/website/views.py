from django.shortcuts import render
from vehicules.models import Vehicule


def home(request):
    vehicules = Vehicule.objects.filter(
        disponible=True
    ).order_by("-date_creation")

    return render(
        request,
        "website/home.html",
        {
            "vehicules": vehicules
        }
    )