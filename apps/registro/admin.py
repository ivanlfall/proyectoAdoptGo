from django.contrib import admin
from apps.registro.models import Denuncia, Posteo, ReferenciaUsuario
# Register your models here.


admin.site.register(Posteo)
admin.site.register(Denuncia)
admin.site.register(ReferenciaUsuario)
