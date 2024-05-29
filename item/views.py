from django.shortcuts import render
from .models import Stock

def grafico(request):
    repuestos = Stock.objects.all()
    total_repuestos=repuestos.count()

    repuestos_cambaceres = repuestos.filter(equipo_asociado__planta='CAMBACERES')
    totales_cambaceres = repuestos.filter(equipo_asociado__planta='CAMBACERES').count()
    repuestos_quilmes = repuestos.filter(equipo_asociado__planta='QUILMES')
    totales_quilmes = repuestos.filter(equipo_asociado__planta='QUILMES').count()
    repuestos_rivadavia = repuestos.filter(equipo_asociado__planta='RIVADAVIA')
    totales_rivadavia = repuestos.filter(equipo_asociado__planta='RIVADAVIA').count()
    
    return render(request, 'item/graficos.html', {
        'total_repuestos': total_repuestos,
        'repuestos_cambaceres': repuestos_cambaceres,
        'totales_cambaceres': totales_cambaceres,
        'repuestos_quilmes': repuestos_quilmes,
        'totales_quilmes': totales_quilmes,
        'repuestos_rivadavia': repuestos_rivadavia,
        'totales_rivadavia': totales_rivadavia
    })
