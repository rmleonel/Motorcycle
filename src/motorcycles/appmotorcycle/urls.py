from django.urls import path
from appmotorcycle.views import(
    index,
    luxury,
    medium,
    economy,
)

urlpatterns = [
    path("luxury/", luxury, name="luxury"),
    path("medium/", medium, name="medium"),
    path("economy/", economy, name="economy"),
    path("", index, name="index"),
]