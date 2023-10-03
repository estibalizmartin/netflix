from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_forms),
    path('new/', views.create_form, name='create_form'),
    path('delete_form/<int:id_formulario>/', views.delete_form, name='delete_form')
]