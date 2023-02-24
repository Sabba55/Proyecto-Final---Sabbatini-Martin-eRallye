from django.urls import path

from AppSabba.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("inicio/", inicio, name="Start"),
    path("sobre_mi/", sobreMi, name="Yo"),



    #autenticacion
    path("registro/", registro, name="Sign Up"),
    path("login/", iniciar_sesion, name="Sign In"),
    path("logout/", LogoutView.as_view(template_name="AppSabba/autenticacion/logout.html"), name="Logout"), #ya importado en esta vista


    #CRUD DE PILOTOS
    path("pilotos/lista", PilotoLista.as_view(), name = "Ver Pilotos"),
    path("pilotos/nuevo", PilotoCrear.as_view(), name = "Crear Pilotos"),
    path("pilotos/borrar/<int:pk>", PilotoBorrar.as_view(), name="Borrar Pilotos"),
    path("pilotos/editar/<int:pk>", PilotoEditar.as_view(), name="Editar Pilotos"),
    
    path("buscar_piloto/", buscar_piloto, name="Buscar Piloto"),
    path("resultados_piloto/", resultadosPiloto, name="Buscar Pilotos"),


    #CRUD DE COPILOTOS
    path("copilotos/lista", CopilotoLista.as_view(), name = "Ver Copilotos"),
    path("copilotos/nuevo", CopilotoCrear.as_view(), name = "Crear Copilotos"),
    path("copilotos/borrar/<int:pk>", CopilotoBorrar.as_view(), name="Borrar Copilotos"),
    path("copilotos/editar/<int:pk>", CopilotoEditar.as_view(), name="Editar Copilotos"),

    path("buscar_copiloto/", buscar_copiloto, name="Buscar Copiloto"),
    path("resultados_copiloto/", resultadosCopiloto, name="Buscar Copilotos"),

    #CRUD DE COPILOTOS
    path("competencia/lista", CompetenciaLista.as_view(), name = "Ver Competencias"),
    path("competencia/nuevo", CompetenciaCrear.as_view(), name = "Crear Competencias"),
    path("competencia/borrar/<int:pk>", CompetenciaBorrar.as_view(), name="Borrar Competencias"),
    path("competencia/editar/<int:pk>", CompetenciaEditar.as_view(), name="Editar Competencias"),

    path("buscar_competencia/", buscar_competencia, name="Buscar Competencia"),
    path("resultados_competencia/", resultadosCompetencia, name="Buscar Competencias"),

]
