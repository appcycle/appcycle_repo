from django.conf.urls import url
from django.contrib.auth.decorators import permission_required

from django.urls import path

from apps.criarusuario.views import signup, ListUsuariosRegistrados, DeleteUser

urlpatterns = [

    path('criarusuario/', signup, name='signup'),
    path('user_list.html', ListUsuariosRegistrados.as_view(), name='listausuarios'),
    path('apagarusuario/<int:pk>/', permission_required('auth.delete_user', login_url='login')(DeleteUser.as_view()), name='apagarusuario'),



]