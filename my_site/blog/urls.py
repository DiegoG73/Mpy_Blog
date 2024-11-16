from django.urls import path
from . import views

urlpatterns = [
    # "path()" nos indica la dirección/ruta en la que podremos ir
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    # "<slug>" es el nombre que se le asigna al concepto de un elemento dinámico en estos contextos (amigable para el navegador)
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]