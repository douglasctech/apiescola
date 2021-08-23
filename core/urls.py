
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunoViewSet, ProfessorViewSet
from rest_framework import routers

router1 = routers.DefaultRouter()
router1.register(r'alunos', AlunoViewSet)
router1.register(r'professores', ProfessorViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router1.urls)),
    
]
