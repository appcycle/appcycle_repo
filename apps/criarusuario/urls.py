from django.conf.urls import url
from django.urls import path

from apps.criarusuario.views import signup, ListUsuariosRegistrados
urlpatterns = [

    path('criarusuario/', signup, name='signup'),
    path('user_list.html', ListUsuariosRegistrados.as_view(), name='listausuarios'),



]