from django.urls import path
from .views import CelularesView, ContatoView, IndexView, DetalhesView, ManutencaoView, cadastro
from django.contrib.auth import views
from aplic.forms import UserLoginForm

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("detalhes", DetalhesView.as_view(), name="detalhes"),
    path("contato", ContatoView.as_view(), name="contato"),
    path("celulares", CelularesView.as_view(), name="celulares"),
    path("manuntencao", ManutencaoView.as_view(), name="manuntencao"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path("cadastro/", cadastro, name="cadastro")
]