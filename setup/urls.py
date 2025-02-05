from django.contrib import admin
from django.urls import path, include
from escola.views import EstudantesViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudantesViewSet,basename='Estudantes')
router.register('cursos', CursoViewSet,basename='Cursos')
router.register('matriculas', MatriculaViewSet,basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',ListaMatriculaCurso.as_view()),
]


