from django.urls import path
from personas.views import PersonasListView, PersonasDeleteView,PersonascreateView, PersonasUpdateView

app_name= 'personas'

urlpatterns = [
    path('', PersonasListView.as_view(), name='index'),
    path('eliminar/<int:pk>', PersonasDeleteView.as_view(), name='eliminar'),
    path('crear', PersonascreateView.as_view(), name='crear'),
    path('editar/<int:pk>', PersonasUpdateView.as_view(), name='editar'),
]
