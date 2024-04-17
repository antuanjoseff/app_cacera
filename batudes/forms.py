from batudes.models import Coto, Sector, Batuda
from django.urls import reverse_lazy
from django import forms

class SectorAdminForm(forms.ModelForm):
    class Meta:
        model = Sector
        htmx_attrs = {
            "hx-get": reverse_lazy("get_coto_bbox"),
            "hx-swap": "none",
            "hx-trigger": "load,change",
            "hx-target": "",
        }

        fields = "__all__"

        widgets = {
            "coto": forms.Select(attrs=htmx_attrs),
        }

class BatudaAdminForm(forms.ModelForm):
    class Meta:
        exclude = ['user',]
        model = Batuda        
        htmx_attrs = {
            "hx-get": reverse_lazy("get_sectors"),
            "hx-swap": "innerHTML",
            "hx-trigger": "load,change",
            "hx-target": "#id_sectors",
        }

        fields = "__all__"

        widgets = {
            "coto": forms.Select(attrs=htmx_attrs),
        }
