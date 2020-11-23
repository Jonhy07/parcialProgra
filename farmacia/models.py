# company/models.py
from django.db import models
# City where employees live
class Proveedor(models.Model):
    proveedor_nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.proveedor_nombre
# Employee title
class CasaMedica(models.Model):
    casa_medica = models.CharField(max_length=100)
    def __str__(self):
        return self.casa_medica
class Medicamento(models.Model):
    medicamento_nombre = models.CharField(max_length=255)
    medicamento_proveedor = models.ForeignKey(Proveedor, related_name='medicamento_proveedor', on_delete=models.CASCADE)
    medicamento_casa = models.ForeignKey(CasaMedica, related_name='medicamento_casa', on_delete=models.CASCADE)
    def __str__(self):
       return self.medicamento_nombre