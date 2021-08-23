from escola.serializer import AlunoSerializer, ProfessorSerializer
from rest_framework import viewsets
from escola.models import Aluno
from escola.models import Professor

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer