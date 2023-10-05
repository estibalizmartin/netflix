from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Formulario, Usuario

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
            request, "list_forms.html", {"formularios": formularios, "error": "Email, asunto y descripción son requeridos."}
        )
    formulario = Formulario(email=new_email, asunto=new_asunto, descripcion=new_descripcion)
    formulario.save()
    return redirect("/forms/")

def delete_form(request, id_formulario):
    try:
        formulario = Formulario.objects.get(id_formulario = id_formulario)
        formulario.delete()
    except ObjectDoesNotExist:
        print("El usuario no existe.")
    return redirect("/forms/")