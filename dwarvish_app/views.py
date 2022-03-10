from django.shortcuts import render

def lesson_index(request):
    return render(request, 'lesson_index.html', {})


def index(request):
    return render(request, 'lesson1/index.html', {})