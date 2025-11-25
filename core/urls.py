from django.urls import path
from .views import (
    CatequizandoDetailView,
    CatequizandoUpdateView,
    CatequizandoCreateView,
    catequizando_buscar,
    catequizando_eliminar,
    catequizando_listar
)

urlpatterns = [
    # LISTAR
    path("", catequizando_listar, name="catequizando_listar"),

    # DETALLE
    path(
        '<int:pk>/detalle/',
        CatequizandoDetailView.as_view(),
        name='catequizando_detalle'
    ),

    # EDITAR
    path(
        '<int:pk>/editar/',
        CatequizandoUpdateView.as_view(),
        name='catequizando_editar'
    ),

    # CREAR (usa SP)
    path(
        'crear/',
        CatequizandoCreateView.as_view(),
        name='catequizando_crear'
    ),
    
    path("<int:persona_id>/eliminar/", catequizando_eliminar, name="catequizando_eliminar"),
    path("buscar/", catequizando_buscar, name="catequizando_buscar"),


]
