from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from .models import Formulario, Usuario, Pelicula, Usuariopelicula

pagina_secundaria = "/forms"
pagina_principal = "/films"
errores = { "campos_requeridos": "Email, asunto y descripción son campos requeridos.", 
            "form_not_found": "Formulario inexistente."}

def list_forms(request):
    formularios = Formulario.objects.all()
    print(formularios)
    return render(request, 'list_forms.html', { "formularios": formularios })

def create_form(request):
    new_email = request.POST["email"] 
    new_asunto = request.POST["asunto"]
    new_descripcion = request.POST["descripcion"]

    try:
        Usuario.objects.get(email=new_email)
    except ObjectDoesNotExist:
        Usuario(
            nombre=None, 
            apellidos=None, 
            email=new_email
        ).save()
        
    if new_email == "" or new_asunto == "" or new_descripcion == "":
        formularios = Formulario.objects.all()
        return render(
            request, "list_forms.html", { "formularios": formularios, "error": errores['campos_requeridos'] }
        )
    else:
        formulario = Formulario(
            email=Usuario.objects.get(email=new_email), 
            asunto=new_asunto, 
            descripcion=new_descripcion
        )
        formulario.save()
        return redirect(pagina_secundaria)

def delete_form(request, id_formulario):
    try:
        formulario = Formulario.objects.get(id_formulario = id_formulario)
        formulario.delete()
    except ObjectDoesNotExist:
        formularios = Formulario.objects.all()
        return render(
            request, "list_forms.html", { "formularios": formularios, "error": errores['form_not_found'] }
        )
    return redirect(pagina_secundaria)

def list_films(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'list_films.html', { "peliculas": peliculas })

def seed_data(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f'SET search_path = netflix')
            cursor.execute(f'CALL CrearRegistros()')

        peliculas = Pelicula.objects.all()
        return render(request, 'list_films.html', { "peliculas": peliculas })
    except:
        print("Vacía la base de datos.")
        return redirect(pagina_principal)

def create_usuariopelicula(request):
    usuario = Usuario.objects.get(id_usuario=1)
    pelicula = Pelicula.objects.get(id_pelicula=1)

    usuariopelicula = Usuariopelicula(
        estado=True,
        fechaestado="2023-10-10",
        id_usuario=usuario,
        id_pelicula=pelicula,
        calificacion=2
    )
    usuariopelicula.save()
    return redirect(pagina_principal)