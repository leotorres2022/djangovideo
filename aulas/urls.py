
from django.urls import path
from .views import hello, bye ,edad, segunda_plantilla, tercer_plantilla, cuarta_plantilla



urlpatterns = [

    path('hello', hello ),
    path('bye', bye ),
    path('edad/<int:edad>/<int:futuro>', edad ),
    path('plantilla', segunda_plantilla ),
    path('tercerplantilla', tercer_plantilla ),
    path('cuartaplantilla', cuarta_plantilla ),
]
