from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.core.exceptions import ValidationError

class Equipo_Asociado(models.Model):
    LOCACION_CHOICES = (
        ('CAMBACERES', 'Cambaceres'),
        ('QUILMES', 'Quilmes'),
        ('RIVADAVIA', 'Rivadavia'),
    )
    nombre=models.CharField(max_length=100, blank=False)
    activo= models.BooleanField(default=True)
    planta = models.CharField(max_length=20, choices=LOCACION_CHOICES, blank=False, null=False)

    class Meta:
        verbose_name = 'Equipo Asociado'
        verbose_name_plural = 'Equipos Asociados'

    def __str__(self):
        return self.nombre +' - ' + self.planta

class Stock(models.Model):
    repuesto_id=models.CharField(max_length=10,primary_key=True)
    descripcion = models.CharField(max_length=150,blank=True, null=True, verbose_name='Descripción')
    equipo_asociado = models.ForeignKey(Equipo_Asociado,on_delete=models.CASCADE, null=True, blank=True)
    stock_real = models.IntegerField(default=0, verbose_name='STOCK')
    stock_minimo = models.IntegerField(default=0, verbose_name='Stock mínimo')
    stock_maximo = models.IntegerField(default=0, verbose_name='Stock Máximo')
    punto_de_reposicion = models.IntegerField(default=0, verbose_name='Punto de reposición')
    ubicacion_fisica= models.CharField(max_length=150,null=True,blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            self.modified_by = user

        super(Stock, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Stock de Repuesto'
        verbose_name_plural = 'Stocks de Repuestos'

    def __str__(self):
        return self.repuesto_id
    
class StockAudit(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,verbose_name='REPUESTO')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha movimiento')
    action = models.CharField(max_length=50, verbose_name='Acción')
    cantidad = models.IntegerField(verbose_name='STOCK')

    class Meta:
        verbose_name = 'Movimiento de Stock'
        verbose_name_plural = 'Movimientos de Stocks'


    def __str__(self):
        return f"{self.user} - {self.action} - {self.stock} - {self.timestamp}"