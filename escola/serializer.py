from rest_framework import serializers
from escola.models import Aluno
from escola.models import Professor


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields =  ['id', 'nome', 'rg']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields =  ['id', 'nome', 'rg']