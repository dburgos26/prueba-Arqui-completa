from django.urls import path
from .views import buscar_frase

urlpatterns = [
    path('buscar_frase/', buscar_frase, name='buscar_frase'),
]