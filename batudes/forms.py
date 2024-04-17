from batudes.models import Coto, Sector, Batuda
from django.urls import reverse_lazy
from django import forms
from django.contrib.gis.forms.widgets import OSMWidget
from django.forms.widgets import HiddenInput

class CustomGeoWidget(OSMWidget):
    template_name = 'gis/custom_openlayers.html'

class CustomHiddenWidget(HiddenInput):
    template_name = 'gis/hidden_input.html'

class CotoAdminForm(forms.ModelForm):
  class Meta:
        model = Coto
        fields = "__all__"


class SectorAdminForm(forms.ModelForm):
    bbox = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Sector
        htmx_attrs = {
            "hx-get": reverse_lazy("get_coto_bbox"),
            "hx-swap": "outerHTML",
            "hx-trigger": "load,change",
            "hx-target": "#id_bbox",
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
