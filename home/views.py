from django.shortcuts import render, redirect
from .models import Especializacion, Curso, Profesor, Alumno
from .forms import EspecializacionForm, CursoForm, ProfesorForm, AlumnoForm, SearchForm

def inicio(request):
    return render(request, 'home/index.html')

def profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor')
    else:
        form = ProfesorForm()
    return render(request, 'home/profesores.html', {'form': form})

def alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno')
    else:
        form = AlumnoForm()
    return render(request, 'home/alumnos.html', {'form': form})

def especializacion(request):
    if request.method == 'POST':
        form = EspecializacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('especializacion')
    else:
        form = EspecializacionForm()
    return render(request, 'home/especializacion.html', {'form': form})

def curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso')
    else:
        form = CursoForm()
    return render(request, 'home/cursos.html', {'form': form})

def buscar(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = {
                'especializaciones': Especializacion.objects.filter(nombre_de_especializacion__icontains=query),
                'cursos': Curso.objects.filter(nombre_del_curso__icontains=query),
                'profesores': Profesor.objects.filter(nombre_completo__icontains=query),
                'alumnos': Alumno.objects.filter(nombre_completo__icontains=query),
            }
            return render(request, 'home/resultados.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'home/buscar.html', {'form': form})
