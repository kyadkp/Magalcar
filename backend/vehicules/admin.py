from django.contrib import admin
from .models import Proprietaire, Categorie, Vehicule, ImageVehicule


@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ("nom", "telephone", "email")
    search_fields = ("nom", "telephone")


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom",)


class ImageVehiculeInline(admin.TabularInline):
    model = ImageVehicule
    extra = 1


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = (
        "marque",
        "modele",
        "categorie",
        "proprietaire",
        "prix_par_jour",
        "disponible",
    )

    list_filter = (
        "categorie",
        "disponible",
        "carburant",
        "transmission",
    )

    search_fields = (
        "marque",
        "modele",
        "localisation",
    )

    inlines = [ImageVehiculeInline]


@admin.register(ImageVehicule)
class ImageVehiculeAdmin(admin.ModelAdmin):
    list_display = (
        "vehicule",
        "principale",
    )