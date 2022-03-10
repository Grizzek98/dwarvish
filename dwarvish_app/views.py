from django.shortcuts import render
from dwarvish_app.models import Lesson

def lesson_index(request):
    lessons = Lesson.objects.all().order_by('-title')
    context = {'lessons': lessons}
    return render(request, 'lesson_index.html', context)

def lesson_detail(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    context = {'lesson': lesson}
    return render(request, 'lesson_detail.html', context)

def index(request):
    return render(request, 'lesson1/index.html', {})