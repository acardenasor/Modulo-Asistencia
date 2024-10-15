from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.show_index),
    path('login/', views.show_login, name='login'),
    path('cursos/', views.show_cursos, name='cursos'),
    path('cursos/<str:codigo_curso>/', views.show_curso, name='curso'),
    path('cursos/<str:codigo_curso>/asistencia', views.registrar_asistencia_curso, name='lista_estudiantes_curso'),
    path('cursos/<str:codigo_curso>/asistencia/historial', views.historial_asistencia_curso, name='asistencia_curso'),
    path('historial', views.historial_asistencia, name='historial'),
    path('logout/', views.logout_view, name='logout'),
    path('verificar_asistencia/', views.verificar_asistencia, name='verificar_asistencia'),
]
