from django.urls import path
from personas.views import *

app_name= 'personas'

urlpatterns = [
    path('', PersonasListView.as_view(), name='index'),
    path('eliminar/<int:pk>', PersonasDeleteView.as_view(), name='eliminar'),
    path('crear', PersonasCreateView.as_view(), name='crear'),
    path('editar/<int:pk>', PersonasUpdateView.as_view(), name='editar'),
    
    path('area/', AreaListView.as_view(), name='area'),
    path('area/eliminar/<int:pk>', AreaDeleteView.as_view(), name='areaeliminar'),
    path('area/crear', AreaCreateView.as_view(), name='areacrear'),
    path('area/editar/<int:pk>', AreaUpdateView.as_view(), name='areaeditar'),
    
    path('departamento/', DepartamentoListView.as_view(), name='departamento'),
    path('departamento/eliminar/<int:pk>', DepartamentoDeleteView.as_view(), name='departamentoeliminar'),
    path('departamento/crear', DepartamentoCreateView.as_view(), name='departamentocrear'),
    path('departamento/editar/<int:pk>', DepartamentoUpdateView.as_view(), name='departamentoeditar'),
    ]

