from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.list_forms),
    path('forms/new/', views.create_form, name='create_form'),
    path('forms/delete/<int:id_formulario>/', views.delete_form, name='delete_form'),
    path('films/', views.list_films),
    path('films/new/', views.create_usuariopelicula),
    path('seeding/', views.seed_data)
]