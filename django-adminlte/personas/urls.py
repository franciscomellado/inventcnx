from django.urls import path
from . import views
from personas.views import Personaindex

urlpatterns = [
    path("", Personaindex.as_view(), name="Personaindex"),
]
