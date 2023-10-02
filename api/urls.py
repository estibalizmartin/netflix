from django.urls import path
from .views import list_users, create_user, delete_user

urlpatterns = [
    path('', list_users),
    path('new/', create_user, name='create_user'),
    path('delete_task/<int:id_usuario>', delete_user, name='delete_user')
]