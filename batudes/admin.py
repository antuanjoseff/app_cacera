from django.contrib.gis import admin
from django.contrib.gis.forms.widgets import OSMWidget
from batudes.models import Coto, Sector, Batuda
from batudes.forms import BatudaAdminForm, SectorAdminForm

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
    form = SectorAdminForm

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

@admin.register(Batuda)
class BatudaAdmin(admin.ModelAdmin):
    form = BatudaAdminForm

    def save_model(self, request, obj, form, change):
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
