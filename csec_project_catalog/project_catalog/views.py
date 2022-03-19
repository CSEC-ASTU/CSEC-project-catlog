from django.shortcuts import render, redirect
from .models import Project
from .forms import EmployeeForm
from django.db.models import Q


def employees_list(request):

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    project = Project.objects.filter(
        Q(title__icontains=search_query)
    )

    context = {
        'project': project,
        'search_query': search_query,
    }
    return render(request, 'list.html', context)


def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_employee(request, pk):
    project = Project.objects.get(id=pk)
    form = EmployeeForm(instance=project)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'edit.html', context)


def delete_employee(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('employees-list')

    context = {
        'project': project,
    }
    return render(request, 'delete.html', context)
