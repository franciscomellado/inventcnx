from django.urls import path
from personas.views import Personasindex

urlpatterns = [
    path('', Personasindex.as_view(), name='personasindex'),
    
]
