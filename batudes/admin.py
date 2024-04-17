from django.contrib.gis import admin
from django.forms import Form, HiddenInput, CharField, ChoiceField, ModelForm
from batudes.models import Coto, Sector, Batuda
from batudes.forms import BatudaAdminForm, SectorAdminForm, CotoAdminForm, CustomGeoWidget
from django.contrib.gis.db.models import Extent
from shapely.geometry import Polygon
import shapely.wkt


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
    form = CotoAdminForm

    def save_model(self, request, obj, form, change):
        # qs = Coto.objects.filter(short_code=obj.short_code).aggregate(Extent("geom"))
        # obj.bbox = obj.geom.Extent
        geom_arr = str(obj.geom).split(';')
        P = shapely.wkt.loads(geom_arr[1])
        obj.bbox = P.bounds

        super().save_model(request, obj, form, change)    

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
