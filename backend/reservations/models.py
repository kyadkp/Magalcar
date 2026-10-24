from django.db import models
from vehicules.models import Vehicule


class Reservation(models.Model):

    STATUTS = [
        ("attente", "En attente"),
        ("confirmee", "Confirmée"),
        ("annulee", "Annulée"),
    ]

    vehicule = models.ForeignKey(
        Vehicule,
        on_delete=models.CASCADE
    )

    nom_client = models.CharField(max_length=100)

    email = models.EmailField()

    telephone = models.CharField(max_length=20)

    date_depart = models.DateField()

    date_retour = models.DateField()

    lieu_depart = models.CharField(max_length=200)

    lieu_retour = models.CharField(max_length=200)

    montant = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUTS,
        default="attente"
    )

    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_client} - {self.vehicule}"