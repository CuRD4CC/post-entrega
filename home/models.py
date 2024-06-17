from django.db import models


class Especializacion(models.Model):
    nombre_de_especializacion = models.CharField(max_length=100)
    duracion = models.CharField(max_length=20)
    campo_de_estudio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_de_especializacion} ({self.duracion}, {self.campo_de_estudio})"

class Curso(models.Model):
    nombre_del_curso = models.CharField(max_length=100)
    duracion = models.CharField(max_length=20)
    profesor_a_cargo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_del_curso} - Duración: {self.duracion} - Profesor: {self.profesor_a_cargo}"

class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=100)
    materia_que_dicta = models.CharField(max_length=100)
    años_de_experiencia = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_completo} - Materia: {self.materia_que_dicta}, Años de experiencia: {self.años_de_experiencia}"

class Alumno(models.Model):
    nombre_completo = models.CharField(max_length=100)
    tipo_especializacion = models.CharField(max_length=100)
    año_de_ingreso = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_completo} - Especialización: {self.tipo_especializacion}, Año de ingreso: {self.año_de_ingreso}"

