from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from .models import Formulario, Usuario, Pelicula

pagina_principal = "/forms"
errores = { "campos_requeridos": "Email, asunto y descripción son campos requeridos.", 
            "form_not_found": "Formulario inexistente."}

def list_forms(request):
    formularios = Formulario.objects.all()
    print(formularios)
    return render(request, 'list_forms.html', { "formularios": formularios })

def create_form(request):
    usuario = Usuario.objects.get(email=request.POST["email"])
    if usuario is None:
        Usuario(nombre=None, apellidos=None, email=request.POST["email"]).save()
    new_asunto = request.POST["asunto"]
    new_descripcion = request.POST["descripcion"]

    if usuario == "" or new_asunto == "" or new_descripcion == "":
        formularios = Formulario.objects.all()
        return render(
            request, "list_forms.html", { "formularios": formularios, "error": errores['campos_requeridos'] }
        )
    formulario = Formulario(email=usuario, asunto=new_asunto, descripcion=new_descripcion)
    formulario.save()
    return redirect(pagina_principal)

def delete_form(request, id_formulario):
    try:
        formulario = Formulario.objects.get(id_formulario = id_formulario)
        formulario.delete()
    except ObjectDoesNotExist:
        formularios = Formulario.objects.all()
        return render(
            request, "list_forms.html", { "formularios": formularios, "error": errores['form_not_found']}
        )
    return redirect(pagina_principal)

def list_films(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'list_films.html', { "peliculas": peliculas })

def seed_data(request):
    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path = netflix')
        cursor.execute(f'CALL CrearRegistros()')

    peliculas = Pelicula.objects.all()
    return render(request, 'list_films.html', { "peliculas": peliculas })