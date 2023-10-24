from django.urls import path
from personas.views import ( 
                            PersonasListView, 
                            PersonasUpdateView, 
                            PersonasCreateView, 
                            PersonasDeleteView)

app_name = 'personas'

urlpatterns = [
    path("", PersonasListView.as_view(), name="index"),
    path("editar/<int:pk>/", PersonasUpdateView.as_view(), name="editar"),
    path("crear/", PersonasCreateView.as_view(), name="crear"),
    path("eliminar/<int:pk>/", PersonasDeleteView.as_view(), name="eliminar"),
    
]
