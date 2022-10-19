from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from inicio.models import Mesa


def inicio(request):
    return render(request, 'inicio/inicio.html')


class ListarMesas(ListView):
    model = Mesa
    template_name = 'inicio/listar_mesas.html'


class CrearMesa(CreateView):
    model = Mesa
    template_name = 'inicio/crear_mesa.html'
    success_url = '/mesas'
    fields = ['material', 'color', 'cant_patas']
    

class EditarMesa(UpdateView):
    model = Mesa
    template_name = 'inicio/editar_mesa.html'
    success_url = '/mesas'
    fields = ['material', 'color', 'cant_patas']
    

class EliminarMesa(DeleteView):
    model = Mesa
    template_name = 'inicio/eliminar_mesa.html'
    success_url = '/mesas'