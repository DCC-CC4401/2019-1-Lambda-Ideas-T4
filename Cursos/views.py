from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView

from .forms import AddCurso
from .models import Curso


def post_cursos(request):
    form = AddCurso()
    return render(request,'cursos/cursos_admin.html', {'form': form})

def add_curso(request):
    if request.POST:
        form = AddCurso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('cursos')
        else:
            form = AddCurso()

    
    return render(request, 'cursos/cursos_admin.html', {'form': form})

def all_cursos(request):
    cursos = Curso.objects.all()
    cursos_list = []

    for curso in cursos:
        cursos_list.append(curso)

    form = AddCurso()

    return render(request, 'blog/cursos.html', {'cursos': cursos_list, 'form':form})