from django.urls import path
from .views import PersonaList, CrearPersona, ActualizarPersona, PersonaByDocumento, EliminarPersona, TareaList, CrearTarea

urlpatterns = [
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/crear/', CrearPersona.as_view(), name='crear-persona'),
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='actualizar-persona'),
    path('personas/buscar/<str:documento>/', PersonaByDocumento.as_view(), name='buscar-persona'),
    path('personas/eliminar/<int:pk>/', EliminarPersona.as_view(), name='eliminar-persona'),
    path('tareas/', TareaList.as_view(), name='tarea-list'),
    path('tareas/crear/',CrearTarea.as_view(), name='crear-tarea'),

]

