from django.urls import path
from appmotorcycle.views import(
    index,
    luxury,
    medium,
    economy,
    formulario,
)

urlpatterns = [
    path("luxury/", luxury, name="luxury"),
    path("medium/", medium, name="medium"),
    path("economy/", economy, name="economy"),
    path("formulario/", formulario, name = 'formulario'),
    path("", index, name="index"),
]