from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Restaurante

# Create your views here.

class RestaurantesView(View):

	def get(self, request):
			restaurantes = Restaurante.objects.all()

			template_name = 'restaurantes/lista.html'

			context = {
				'restaurantes':restaurantes
			}

			return render(request, template_name, context)

class DetailRestView(View):
	def get(self, request, id):

		restaurante = get_object_or_404(Restaurante, id=id)

		template_name = 'restaurantes/detalle.html'

		context = {
			'restaurante': restaurante
		}

		return render(request, template_name, context)


