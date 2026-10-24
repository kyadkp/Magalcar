from django.db import models


class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Vehicule(models.Model):

    TRANSMISSIONS = [
        ("Manuelle", "Manuelle"),
        ("Automatique", "Automatique"),
    ]

    CARBURANTS = [
        ("Essence", "Essence"),
        ("Diesel", "Diesel"),
        ("Hybride", "Hybride"),
        ("Electrique", "Electrique"),
    ]

    proprietaire = models.ForeignKey(
        Proprietaire,
        on_delete=models.CASCADE,
        related_name="vehicules"
    )

    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.PositiveIntegerField()
    couleur = models.CharField(max_length=50)

    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSIONS
    )

    carburant = models.CharField(
        max_length=20,
        choices=CARBURANTS
    )

    nombre_places = models.PositiveIntegerField()

    prix_par_jour = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    localisation = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    disponible = models.BooleanField(default=True)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marque} {self.modele}"


class ImageVehicule(models.Model):
    vehicule = models.ForeignKey(
        Vehicule,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="vehicules/")

    principale = models.BooleanField(default=False)

    def __str__(self):
        return f"Image - {self.vehicule}"