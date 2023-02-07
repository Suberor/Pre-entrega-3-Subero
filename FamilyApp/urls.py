from django.urls import path
from FamilyApp.views import *

urlpatterns = [
    path("inicio/", visualizar, name="inicio"),
    path("hechizos/", spells, name="spells"),
    path("monstruos/", monsters, name="monsters"),
    path("resultados/", resultados, name="resultados"),
    path("armas/", weapons, name="weapons"),
]