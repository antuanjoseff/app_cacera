from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_sectors/", views.get_sectors.as_view(), name="get_sectors"),
    path("get_coto_bbox/", views.get_coto_bbox, name="get_coto_bbox"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






