from django.contrib import admin
from .models import *

class ProveedorAdmin(admin.ModelAdmin):
    fields = ('proveedor_nombre',)
class CasaMedicaAdmin(admin.ModelAdmin):
    fields = ('casa_medica',)
class MedicamentoAdmin(admin.ModelAdmin):
    fields = ('medicamento_nombre','medicamento_proveedor','medicamento_casa',)

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(CasaMedica, CasaMedicaAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)