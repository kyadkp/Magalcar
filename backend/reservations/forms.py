from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation

        fields = [
            "nom_client",
            "email",
            "telephone",
            "date_depart",
            "date_retour",
            "lieu_depart",
            "lieu_retour",
        ]

widgets = {
    "nom_client": forms.TextInput(attrs={"class": "form-control"}),
    "email": forms.EmailInput(attrs={"class": "form-control"}),
    "telephone": forms.TextInput(attrs={"class": "form-control"}),
    "date_depart": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    "date_retour": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    "lieu_depart": forms.TextInput(attrs={"class": "form-control"}),
    "lieu_retour": forms.TextInput(attrs={"class": "form-control"}),
}