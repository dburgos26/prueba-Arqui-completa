from django.shortcuts import render
from .models import Frase

def buscar_frase(request):
    if request.method == 'POST':
        palabra = request.POST.get('palabra')
        try:
            frase = Frase.objects.get(palabra=palabra)
        except Frase.DoesNotExist:
            mensaje = f"No se encontró una frase para la palabra '{palabra}'."
            return render(request, 'buscar_frase.html', {'mensaje': mensaje})
        else:
            return render(request, 'buscar_frase.html', {'frase': frase.frase})
    else:
        return render(request, 'buscar_frase.html')