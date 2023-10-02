from django.shortcuts import render, redirect
from .models import Usuario

def list_users(request):
    usuarios = Usuario.objects.all()
    return render(request, 'list_users.html', { "usuarios": usuarios })

def create_user(request):
    usuario = Usuario(title = request.POST['title'], description = request.POST['description'])
    usuario.save()
    return redirect('/users/')

def delete_user(request, id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)
    usuario.delete()
    return redirect('/users/')