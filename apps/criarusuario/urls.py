from django.conf.urls import url

from apps.criarusuario.views import signup



urlpatterns = [

    url('criarusuario/', signup, name='signup'),


]