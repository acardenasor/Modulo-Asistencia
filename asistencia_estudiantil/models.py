from django.db import models

# Modelo de la tabla Curso
class Curso(models.Model):
    codigo_curso = models.CharField(max_length=10, primary_key=True)  # Ahora es la clave primaria
    nombre_curso = models.CharField(max_length=100)
    
    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.nombre_curso, self.codigo_curso)

# Modelo de la tabla Estudiante
class Estudiante(models.Model):
    id_estudiante = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    def __str__(self):  # 
        txt = "{0} - {1} - ({2})"
        return txt.format(self.nombre, self.id_estudiante, self.curso)

# Modelo de la tabla Asistencia
class Asistencia(models.Model):
    id = models.AutoField(primary_key=True) 
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado_asistencia = models.CharField(max_length=10, choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')])
    
    def __str__(self):  # 
        txt = "{0} - {1} - ({2})"
        return txt.format(self.estudiante.nombre, self.estudiante.curso.nombre_curso, self.fecha)

