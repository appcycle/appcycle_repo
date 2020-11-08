from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.core.views import home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('cadastro/', include('apps.cadastro.urls')),
    path('projeto/', include('apps.projeto.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('dashboard/', include('apps.dashboard.urls')),
    path('requisitos/', include('apps.requisitos.urls')),
    path('gestaoteste/', include('apps.gestaoteste.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

