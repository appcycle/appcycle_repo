from django.contrib import admin

# Register your models here.
from apps.gestaobug.models import StatusBug, SeveridadeBug, GestaoBug

admin.site.register(StatusBug)
admin.site.register(SeveridadeBug)
admin.site.register(GestaoBug)
