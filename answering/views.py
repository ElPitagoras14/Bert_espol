from django.shortcuts import render
from .main import *

# Create your views here.

def pregunta(request):
    historial = cargarHistorial()
    if request.method == 'POST':
        pregunta = request.POST['text']
        categoria = request.POST['combo']
        resultado = respuesta(categoria, pregunta)
        historial = cargarHistorial()
        frec = frecuentes(categoria)
        return render(request, 'index.html', {'pregunta': pregunta, 'respuesta': resultado[0], 'historial': historial, 'frecuentes': frec})
    else:
        frec = frecuentes("historia")
        return render(request, 'index.html', {'historial': historial, 'frecuentes': frec})