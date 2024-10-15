from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse #quitar ahorita
from . models import Curso, Estudiante, Asistencia
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import JsonResponse

@login_required
def verificar_asistencia(request):
    if request.method == 'GET':
        fecha = request.GET.get('fecha')
        codigo_curso = request.GET.get('codigo_curso')
        
        curso = get_object_or_404(Curso, codigo_curso=codigo_curso)
        
        existe_asistencia = Asistencia.objects.filter(fecha=fecha, estudiante__curso=curso).exists()
        
        return JsonResponse({'existe': existe_asistencia})

def show_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cursos')
        else:
            error = "El usuario y la contraseña no coinciden."

    context = {}
    if error is not None:
        context['error'] = error

    return render(request, 'login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def show_cursos(request):
    username = request.user.username
    cursos = Curso.objects.all()
    query = request.GET.get('search', '')
    
    if query:
        cursos = cursos.filter(nombre_curso__icontains=query) | cursos.filter(codigo_curso__icontains=query)
        
    return render(request, 'cursos.html',{
        'username': username,
        'cursos' : cursos,
        'query': query
    }                )

def show_index(request):
    return redirect('/login/')

@login_required
def show_curso(request, codigo_curso):
    username = request.user.username
    curso = get_object_or_404(Curso, codigo_curso=codigo_curso)
    estudiantes = Estudiante.objects.filter(curso=curso)
    return render(request, 'curso.html',{
                'curso': curso,
                'username': username,
                'estudiantes': estudiantes
            })

@login_required
def registrar_asistencia_curso(request, codigo_curso):
    error = None
    username = request.user.username
    curso = get_object_or_404(Curso, codigo_curso=codigo_curso)
    estudiantes = Estudiante.objects.filter(curso=curso)

    if request.method == 'POST':
        fecha = request.POST.get('fecha')

        if fecha:
            if Asistencia.objects.filter(fecha=fecha, estudiante__curso=curso).exists():
                error = 'Ya se ha registrado la asistencia para esta fecha.'
                context = {
                    'curso': curso,
                    'estudiantes': estudiantes,
                    'username': username,
                    'error': error
                }
            else:
                # Registrar asistencia si no existe
                for estudiante in estudiantes:
                    estado = request.POST.get(f'asistencia_{estudiante.id_estudiante}')
                    if estado:  # Asegúrate de que haya un estado
                        Asistencia.objects.create(
                            estudiante=estudiante,
                            fecha=fecha,  # Guardar la fecha validada
                            estado_asistencia=estado
                        )
                return redirect('curso', codigo_curso=codigo_curso)
    
    context = {
        'curso': curso,
        'estudiantes': estudiantes,
        'username': username
    }
    
    if error is not None:
        context['error'] = error
    
    return render(request, 'asistencia_curso.html', context)

@login_required
def historial_asistencia_curso(request, codigo_curso):
    curso = get_object_or_404(Curso, codigo_curso=codigo_curso)
    
    # Obtener todas las asistencias para este curso
    asistencias = Asistencia.objects.filter(estudiante__curso=curso)
    estudiantes = Estudiante.objects.filter(curso=curso).order_by('nombre')

    # Obtener fechas únicas para el filtro
    fechas = asistencias.values_list('fecha', flat=True).distinct().order_by('fecha')

    # Filtrar por estudiante si se seleccionó
    estudiante_id = request.GET.get('estudiante')
    if estudiante_id:
        asistencias = asistencias.filter(estudiante__id_estudiante=estudiante_id)

    # Filtrar por fecha si se seleccionó y no está vacía
    fecha = request.GET.get('fecha')
    if fecha:
        # Asegúrate de que el valor que filtras esté en el mismo formato que las fechas en la base de datos
        asistencias = asistencias.filter(fecha=fecha)

    # Filtrar por estado si se seleccionó
    estado = request.GET.get('estado')
    if estado:
        asistencias = asistencias.filter(estado_asistencia=estado)

    return render(request, 'historial_curso.html', {
        'curso': curso,
        'asistencias': asistencias,
        'estudiantes': estudiantes,
        'fechas': fechas,  # Pasamos las fechas únicas a la plantilla
    })
    
@login_required
def historial_asistencia(request):
    username = request.user.username
    asistencias = Asistencia.objects.all()
    cursos = Curso.objects.all()
    estudiantes = Estudiante.objects.all()
    fechas = Asistencia.objects.values_list('fecha', flat=True).distinct().order_by('fecha')

    # Filtrar por curso si se seleccionó
    curso_id = request.GET.get('curso')
    if curso_id:
        asistencias = asistencias.filter(estudiante__curso__codigo_curso=curso_id)

    # Filtrar por estudiante si se seleccionó
    estudiante_id = request.GET.get('estudiante')
    if estudiante_id:
        asistencias = asistencias.filter(estudiante__id_estudiante=estudiante_id)

    # Filtrar por fecha si se seleccionó
    fecha = request.GET.get('fecha')
    if fecha:
        asistencias = asistencias.filter(fecha=fecha)

    # Filtrar por estado si se seleccionó
    estado = request.GET.get('estado')
    if estado:
        asistencias = asistencias.filter(estado_asistencia=estado)

    return render(request, 'historial.html', {
        'asistencias': asistencias,
        'username' : username,
        'cursos': cursos,
        'estudiantes': estudiantes,
        'fechas': fechas,
    })