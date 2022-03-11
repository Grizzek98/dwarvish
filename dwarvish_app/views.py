from django.shortcuts import render
from rest_framework import viewsets
from .models import Char
from dwarvish_app import serializers

def lesson_index(request):
    return render(request, 'lesson_index.html', {})

def index(request):
    return render(request, 'lesson1/index.html', {})

class CharAll(viewsets.ModelViewSet) :
    serializer_class = serializers.EngCirthSerializer
    queryset = Char.objects.all()
