from django.conf import settings
from django.contrib.gis.db import models

# Create your models here.

def get_default_coto_status():
    return Coto.objects.get_or_create(short_code="GAV")[0]

class Coto(models.Model):
    short_code = models.CharField(max_length=5, unique=True, null=True)
    name = models.CharField(max_length=255)
    geom = models.MultiPolygonField()
    bbox = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Sector(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    coto = models.ForeignKey(Coto, on_delete=models.CASCADE)
    geom = models.MultiPolygonField()

    def __str__(self):
        return "Coto: {} - Sector: {}".format(self.coto.name, self.name)

class Batuda(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    coto = models.ForeignKey(Coto, on_delete=models.CASCADE, default=get_default_coto_status, null=False)
    sectors = models.ManyToManyField(Sector)
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Batudes"
        ordering = ('-date','name')

    def __str__(self):
        return self.name
    
