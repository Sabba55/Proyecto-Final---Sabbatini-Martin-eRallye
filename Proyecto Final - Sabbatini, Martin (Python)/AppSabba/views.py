from django.shortcuts import render

from django.http import HttpResponse
#Importamos de models y de forms
from AppSabba.models import *
from AppSabba.forms import *
#otros importaciones para iniciar sesion
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#def para tener mi app en el inicio
def inicio(request):
    return render(request, "AppSabba/inicio.html")

def sobreMi(request):
    return render(request, "AppSabba/sobre_mi.html")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Registrarse, Iniciar Sesion y Cerrar sesion

def registro(request):

    if request.method == "POST":
        miFormulario = RegistroFormulario(request.POST) #obtener los datos que están en el formulario
    
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, "AppSabba/inicio.html")

    else:
        miFormulario = RegistroFormulario()
    
    return render(request, "AppSabba/autenticacion/registro.html", {"formulario1":miFormulario})


def iniciar_sesion(request):

    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data = request.POST)
    
        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data.get("username") #obteniendo el usuario y la contra ingresados
            contra = miFormulario.cleaned_data.get("password")
            miUsuario = authenticate(username=usuario, password=contra) #autentica que los datos de inicio sean correctos

            if miUsuario:
                login(request, miUsuario)
                mensaje = f"{miUsuario}" #indico el usuario
                return render(request, "AppSabba/inicio.html", {"mensaje":mensaje})

        else: #y si esta mal
            mensaje = f"Ingrese correctamente sus datos."
            return render(request, "AppSabba/inicio.html", {"mensaje":mensaje})

    else:

        miFormulario = AuthenticationForm()
    
    return render(request, "AppSabba/autenticacion/login.html", {"formulario1":miFormulario})


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CRUD DE PILOTOS con vistas basadas en clases

class PilotoLista(ListView): #piloto_list / base de template
    model = Piloto
    template_name = "AppSabba/drivers/piloto_list.html"
#LoginRequiredMixin
class PilotoCrear(LoginRequiredMixin, CreateView): #..._form.html
    model = Piloto
    fields = ["nombre", "apellido", "edad", "nacionalidad", "marca_vehiculo", "modelo_vehiculo"]
    success_url = "/AppSabba/pilotos/lista"
    template_name = "AppSabba/drivers/piloto_form.html"

class PilotoBorrar(LoginRequiredMixin, DeleteView):  #..._confirm_delete.html
    model = Piloto
    success_url = "/AppSabba/pilotos/lista"
    template_name = "AppSabba/drivers/piloto_confirm_delete.html"

class PilotoEditar(LoginRequiredMixin, UpdateView): #..._form.html
    model = Piloto
    fields = ["nombre", "apellido", "edad", "nacionalidad", "marca_vehiculo", "modelo_vehiculo"]
    success_url = "/AppSabba/pilotos/lista"
    template_name = "AppSabba/drivers/piloto_form.html"

#buscar piloto
def buscar_piloto(request): 
    return render(request, "AppSabba/drivers/busquedaPiloto.html") 

def resultadosPiloto(request):
    if request.method == "GET":

        pilotoBusqueda = request.GET["apellido"] 
        pilotoResultados = Piloto.objects.filter(apellido__icontains=pilotoBusqueda) #pedimos todo su contenido, lo filtramos
        return render(request, "AppSabba/drivers/resultadospiloto.html", {"apellido":pilotoBusqueda, "resultado":pilotoResultados})

    return render(request, "AppSabba/drivers/resultadospiloto.html")

#------------------------------------------------------------------------------------------------------------------------------

#CRUD DE COPILOTO con vistas basadas en clases
class CopilotoLista(ListView): #piloto_list / base de template
    model = Copiloto
    template_name = "AppSabba/codriver/copiloto_list.html"

class CopilotoCrear(LoginRequiredMixin, CreateView): #..._form.html
    model = Copiloto
    fields = ["nombre", "apellido", "edad", "nacionalidad"]
    success_url = "/AppSabba/copilotos/lista"
    template_name = "AppSabba/codriver/copiloto_form.html"

class CopilotoBorrar(LoginRequiredMixin, DeleteView):  #..._confirm_delete.html
    model = Copiloto
    success_url = "/AppSabba/copilotos/lista"
    template_name = "AppSabba/codriver/copiloto_confirm_delete.html"

class CopilotoEditar(LoginRequiredMixin, UpdateView): #..._form.html
    model = Copiloto
    fields = ["nombre", "apellido", "edad", "nacionalidad"]
    success_url = "/AppSabba/copilotos/lista"
    template_name = "AppSabba/codriver/copiloto_form.html"

#buscar copiloto
def buscar_copiloto(request): 
    return render(request, "AppSabba/codriver/busquedaCopiloto.html") 

def resultadosCopiloto(request):
    if request.method == "GET":

        copilotoBusqueda = request.GET["apellido"] 
        copilotoResultados = Copiloto.objects.filter(apellido__icontains=copilotoBusqueda) 
        return render(request, "AppSabba/codriver/resultadoscopiloto.html", {"apellido":copilotoBusqueda, "resultado":copilotoResultados})

    return render(request, "AppSabba/drivers/resultadoscopiloto.html")


#------------------------------------------------------------------------------------------------------------------------------
#CRUD DE COMPETENCIAS con vistas basadas en clases

class CompetenciaLista(ListView): #piloto_list / base de template
    model = Competencia
    template_name = "AppSabba/competencia/competencia_list.html"

class CompetenciaCrear(LoginRequiredMixin, CreateView): #..._form.html
    model = Competencia
    fields = ["nombre", "nacionalidad", "state", "fecha", "inscriptos", "kilometraje", "placa", "imagen"]
    success_url = "/AppSabba/competencia/lista"
    template_name = "AppSabba/competencia/competencia_form.html"

class CompetenciaBorrar(LoginRequiredMixin, DeleteView):  #..._confirm_delete.html
    model = Competencia
    success_url = "/AppSabba/competencia/lista"
    template_name = "AppSabba/competencia/competencia_confirm_delete.html"

class CompetenciaEditar(LoginRequiredMixin, UpdateView): #..._form.html
    model = Competencia
    fields = ["nombre", "nacionalidad", "state", "fecha", "inscriptos", "kilometraje", "placa", "imagen"]
    success_url = "/AppSabba/competencia/lista"
    template_name = "AppSabba/competencia/competencia_form.html"

#buscar rally
def buscar_competencia(request): 
    return render(request, "AppSabba/competencia/busquedaCompetencia.html") 

def resultadosCompetencia(request):
    if request.method == "GET":

        competenciaBusqueda = request.GET["nombre"] 
        competenciaResultados = Competencia.objects.filter(nombre__icontains=competenciaBusqueda) 
        return render(request, "AppSabba/competencia/resultadoscompetencia.html", {"nombre":competenciaBusqueda, "resultado":competenciaResultados})

    return render(request, "AppSabba/competencia/resultadoscompetencia.html")