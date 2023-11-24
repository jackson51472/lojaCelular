from django.urls import path
from .views import IndexView, DetalhesView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("detalhes", DetalhesView.as_view(), name="detalhes"),
]