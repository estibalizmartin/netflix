from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Formulario, Usuario, Pelicula

pagina_principal = "/forms"
errores = { "campos_requeridos": "Email, asunto y descripción son campos requeridos.", 
            "form_not_found": "Formulario inexistente."}

def list_forms(request):
    formularios = Formulario.objects.all()
    return render(request, 'list_forms.html', { "formularios": formularios })

def create_form(request):

    Usuario(nombre=None, apellidos=None, email=request.POST["email"]).save()
    new_email = Usuario.objects.get(email=request.POST["email"])
    new_asunto = request.POST["asunto"]
    new_descripcion = request.POST["descripcion"]

    if new_email == "" or new_asunto == "" or new_descripcion == "":
        formularios = Formulario.objects.all()
        return render(
            request, "list_forms.html", { "formularios": formularios, "error": errores['campos_requeridos'] }
        )
    formulario = Formulario(email=new_email, asunto=new_asunto, descripcion=new_descripcion)
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