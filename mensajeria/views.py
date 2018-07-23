from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import FilesExcel, FotoPerfil
from .forms import SubirArchivo, SubirFoto
from django.utils import timezone

def index(request):
	usuario = request.user
	context = {
		'usuario': usuario,
	}
	return render(request, "mensajeria/index.html", context)

def servicio(request):
	usuario = request.user
	return render(request, "mensajeria/servicio.html", {'usuario':usuario})

def sesion(request):
	return render(request, "mensajeria/sesion.html", {'registro': registro, 'inicios': inicios})


def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/ingresar')
	else:
		formulario = UserCreationForm()
	return render(request, 'mensajeria/sesion.html', {'formulario':formulario})



def ingresar(request):
	#if not request.user.is_anonymous():
	#	return HttpResponseRedirect('/privado')
	if request.method=='POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render(request, 'mensajeria/noactivo.html', {})
			else:
				return render(request, 'mensajeria/nousuario.html', {})
	else:
		formulario = AuthenticationForm()
	return render(request, 'mensajeria/ingresar.html', {'formulario': formulario})



@login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	return render(request, 'mensajeria/privado.html', {'usuario':usuario})



@login_required(login_url='/ingresar')
def files(request):
	usuario = request.user

	excels = FilesExcel.objects.filter(user_iden=usuario)
	
	#ruta = excels.docfile.url

	if request.method=='POST':
		formulario = SubirArchivo(request.POST, request.FILES)
		if formulario.is_valid:
			form = formulario.save(commit=False)
			form.user_iden = usuario
			form.fecha_subida = timezone.now()
			form.save()
			return HttpResponseRedirect('/archivos')
		else:
			return HttpResponseRedirect('/archivos')
	else:
		formulario = SubirArchivo()

	context = {
		'usuario': usuario,
		'excels': excels,
		'formulario': formulario,
	}

	return render(request, 'mensajeria/files.html', context)



@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')



@login_required(login_url='/ingresar')
def archi(request):
	#return HttpResponse(content_type="application/vnd.ms-excel")
	return HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")




@login_required(login_url='/ingresar')
def edit_perejil(request):
	usuario = request.user

	if request.method=='POST':
		formulario = SubirFoto(request.POST, request.FILES)
		if formulario.is_valid:
			form = formulario.save(commit=False)
			form.user = usuario
			#form.fecha_subida = timezone.now()
			form.save()
			return HttpResponseRedirect('/editar-perfil')
		else:
			return HttpResponseRedirect('/editar-perfil')
	else:
		formulario = SubirFoto()

	context = {
		'usuario': usuario,
		'formulario': formulario,
	}
	return render(request, 'mensajeria/edit_perfil.html', context)



@login_required(login_url='/ingresar')
def mensajeria(request):
	usuario = request.user
	context = {
		'usuario' : usuario
	}
	return render(request, 'mensajeria/mensaje.html', context)