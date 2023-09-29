# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Formulario(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='email', to_field='email')
    asunto = models.CharField()
    descripcion = models.TextField()
    id_usuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'formulario'


class Listareproduccion(models.Model):
    id_lista = models.AutoField(primary_key=True)
    nombre = models.CharField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'listareproduccion'


class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    titulo = models.CharField()
    director = models.CharField()
    duracion = models.IntegerField()
    calificacion_promedio = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'pelicula'


class Peliculalistareproduccion(models.Model):
    id_pelicula = models.OneToOneField(Pelicula, models.DO_NOTHING, db_column='id_pelicula', primary_key=True)  # The composite primary key (id_pelicula, id_listareproduccion) found, that is not supported. The first column is selected.
    id_listareproduccion = models.ForeignKey(Listareproduccion, models.DO_NOTHING, db_column='id_listareproduccion')

    class Meta:
        managed = False
        db_table = 'peliculalistareproduccion'
        unique_together = (('id_pelicula', 'id_listareproduccion'),)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField()
    apellidos = models.CharField()
    email = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuariopelicula(models.Model):
    estado = models.BooleanField()
    fechaestado = models.DateField()
    id_usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)  # The composite primary key (id_usuario, id_pelicula) found, that is not supported. The first column is selected.
    id_pelicula = models.ForeignKey(Pelicula, models.DO_NOTHING, db_column='id_pelicula')
    calificacion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuariopelicula'
        unique_together = (('id_usuario', 'id_pelicula'),)
