from django.shortcuts import render
from django.views.generic import ListView
from batudes.models import Coto, Sector

# Create your views here.
def index():
    pass

class get_sectors(ListView):
    model = Sector
    template_name = "batudes/sector_choices.html"
    
    def get_queryset(self):
        if coto_id := self.request.GET.get("coto"):
            try:
                coto = Coto.objects.get(pk=coto_id)
            except Coto.DoesNotExist:
                pass
            else:
                return Sector.objects.filter(coto__id=coto_id).all()
        return Sector.objects.none()