from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#https://docs.djangoproject.com/es/2.0/intro/tutorial04/
#Después de incrementar el conteo de la elección, el código retorna
#una HttpResponseRedirect en lugar de una HttpResponse normal HttpResponseRedirect toma un único argumento:
#La URL a la que el usuario será redirigido (vea el siguiente aspecto de cómo construimos la URL en este caso).

from django.views.decorators.csrf import csrf_exempt
from .models import Pages
# Create your views here.

def barra (request):

	lista = Pages.objects.all()
	respuesta = "<ul>"
	for pagina in lista:
		respuesta += '<li><a href: "/pages/' + str(paginal.id) + '">' + pagina.name + "</a>" 
	respuesta = "</ul>"
	return HttpResponse(respuesta)

@csrf_exempt
def pages (request,num):

	if request.method == "POST":
		page  = Pages (name = request.POST['name'], page = request.POST['pages'])
		page.save()
	try:
		page = Pages.objects.get(id = str(num))	
	except Pages.DoesNotExist:
		return HttpResponseNotFound('<h1>' + num + 'not found</h1>')
	return HttpResponse(page.name + str(page.page))
