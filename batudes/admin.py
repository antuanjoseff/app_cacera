from django.contrib.gis import admin
from django.contrib.gis.forms.widgets import OSMWidget
from batudes.models import Coto, Sector, Batuda
from django.urls import reverse_lazy
from django import forms

class CustomGeoWidget(OSMWidget):
    template_name = 'gis/custom_openlayers.html'

class CustomGeoModelAdmin(admin.GISModelAdmin):
    gis_widget = CustomGeoWidget
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 10,
            'default_lon': 3,
            'default_lat': 41.95,
        },
    }


@admin.register(Coto)
class CotoAdmin(CustomGeoModelAdmin):
    pass

@admin.register(Sector)
class SectorAdmin(CustomGeoModelAdmin):
  
    def get_model_perms(self, request):
        if (not Coto.objects.count()):
            return {}
        else:
            return {
                'add': True,
                'change': True,
                'delete': True,
                'view': True,
            }
        
    pass

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



@admin.register(Batuda)
class BatudaAdmin(admin.ModelAdmin):
    form = BatudaAdminForm

    def save_model(self, request, obj, form, change):
        print('hola mundo ' + request.user.username)
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_model_perms(self, request):
        if (not Sector.objects.count()):
            return {}
        else:
            return {
                'add': True,
                'change': True,
                'delete': True,
                'view': True,
            }

    pass
