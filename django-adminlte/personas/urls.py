from django.urls import path
from personas.views import PersonaListWiews

urlpatterns = [
    path("", PersonaListWiews.as_view(), name="Personaindex"),
]
