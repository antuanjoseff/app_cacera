from django.shortcuts import render
from django.views.generic import ListView
from batudes.models import Coto, Sector
from django.http import HttpResponse

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
    
def get_coto_bbox(request):
    coto_id = request.GET.get('coto', '')
    bbox = Coto.objects.filter(pk=coto_id).values_list('bbox').first()

    return HttpResponse("""
        <input type="text" name="bbox" required="" id="id_bbox" value="{}">
        <script>
           changeMapView()
        </script>
    """.format(bbox))
   