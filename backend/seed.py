import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from vehicules.models import Proprietaire, Categorie, Vehicule

# -----------------------------
# Catégories
# -----------------------------

categories = ["SUV", "Berline", "Pick-up"]

for nom in categories:
    Categorie.objects.get_or_create(nom=nom)

# -----------------------------
# Propriétaires
# -----------------------------

proprietaires = [
    {
        "nom": "Mbeuk Faye",
        "telephone": "770000001",
        "email": "mbeuk@gmail.com"
    },
    {
        "nom": "Cheikh Ndiaye",
        "telephone": "770000002",
        "email": "cheikh@gmail.com"
    },
    {
        "nom": "Mamadou Diallo",
        "telephone": "770000003",
        "email": "mamadou@gmail.com"
    },
]

for p in proprietaires:
    Proprietaire.objects.get_or_create(
        nom=p["nom"],
        defaults={
            "telephone": p["telephone"],
            "email": p["email"]
        }
    )

# -----------------------------
# Récupération
# -----------------------------

suv = Categorie.objects.get(nom="SUV")
berline = Categorie.objects.get(nom="Berline")
pickup = Categorie.objects.get(nom="Pick-up")

mbeuk = Proprietaire.objects.get(nom="Mbeuk Faye")
cheikh = Proprietaire.objects.get(nom="Cheikh Ndiaye")
mamadou = Proprietaire.objects.get(nom="Mamadou Diallo")

# -----------------------------
# Véhicules
# -----------------------------

vehicules = [

    {
        "proprietaire": mbeuk,
        "categorie": suv,
        "marque": "Toyota",
        "modele": "Prado TXL",
        "annee": 2022,
        "couleur": "Noir",
        "transmission": "Automatique",
        "carburant": "Diesel",
        "nombre_places": 7,
        "prix_par_jour": 80000,
        "localisation": "Dakar",
        "description": "Toyota Prado très confortable."
    },

    {
        "proprietaire": mbeuk,
        "categorie": suv,
        "marque": "Hyundai",
        "modele": "Santa Fe",
        "annee": 2023,
        "couleur": "Blanc",
        "transmission": "Automatique",
        "carburant": "Essence",
        "nombre_places": 7,
        "prix_par_jour": 65000,
        "localisation": "Diamniadio",
        "description": "SUV moderne."
    },

    {
        "proprietaire": cheikh,
        "categorie": berline,
        "marque": "Toyota",
        "modele": "Corolla",
        "annee": 2021,
        "couleur": "Gris",
        "transmission": "Automatique",
        "carburant": "Essence",
        "nombre_places": 5,
        "prix_par_jour": 35000,
        "localisation": "Dakar",
        "description": "Très économique."
    },

    {
        "proprietaire": cheikh,
        "categorie": berline,
        "marque": "Mercedes",
        "modele": "Classe C",
        "annee": 2022,
        "couleur": "Noir",
        "transmission": "Automatique",
        "carburant": "Diesel",
        "nombre_places": 5,
        "prix_par_jour": 90000,
        "localisation": "Mbour",
        "description": "Confort premium."
    },

    {
        "proprietaire": mamadou,
        "categorie": pickup,
        "marque": "Toyota",
        "modele": "Hilux",
        "annee": 2023,
        "couleur": "Blanc",
        "transmission": "Manuelle",
        "carburant": "Diesel",
        "nombre_places": 5,
        "prix_par_jour": 70000,
        "localisation": "Thiès",
        "description": "Pick-up robuste."
    },

    {
        "proprietaire": mamadou,
        "categorie": pickup,
        "marque": "Ford",
        "modele": "Ranger",
        "annee": 2022,
        "couleur": "Bleu",
        "transmission": "Automatique",
        "carburant": "Diesel",
        "nombre_places": 5,
        "prix_par_jour": 75000,
        "localisation": "Saint-Louis",
        "description": "Ford Ranger puissant."
    },

    {
        "proprietaire": mbeuk,
        "categorie": suv,
        "marque": "Kia",
        "modele": "Sportage",
        "annee": 2024,
        "couleur": "Rouge",
        "transmission": "Automatique",
        "carburant": "Essence",
        "nombre_places": 5,
        "prix_par_jour": 50000,
        "localisation": "Dakar",
        "description": "SUV élégant."
    },

    {
        "proprietaire": cheikh,
        "categorie": berline,
        "marque": "Hyundai",
        "modele": "Elantra",
        "annee": 2023,
        "couleur": "Blanc",
        "transmission": "Automatique",
        "carburant": "Essence",
        "nombre_places": 5,
        "prix_par_jour": 40000,
        "localisation": "Saly",
        "description": "Berline récente."
    },

    {
        "proprietaire": mamadou,
        "categorie": suv,
        "marque": "Nissan",
        "modele": "Patrol",
        "annee": 2021,
        "couleur": "Noir",
        "transmission": "Automatique",
        "carburant": "Diesel",
        "nombre_places": 7,
        "prix_par_jour": 85000,
        "localisation": "Touba",
        "description": "Idéal pour les longs trajets."
    },

    {
        "proprietaire": mbeuk,
        "categorie": suv,
        "marque": "Range Rover",
        "modele": "Evoque",
        "annee": 2024,
        "couleur": "Gris",
        "transmission": "Automatique",
        "carburant": "Hybride",
        "nombre_places": 5,
        "prix_par_jour": 120000,
        "localisation": "Dakar",
        "description": "SUV de luxe."
    },
]

for v in vehicules:
    Vehicule.objects.get_or_create(
        marque=v["marque"],
        modele=v["modele"],
        defaults=v
    )

print("Base de données remplie avec succès !")