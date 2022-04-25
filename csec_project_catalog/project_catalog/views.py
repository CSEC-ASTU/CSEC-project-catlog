from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import ProjectForm,EventForm

from .models import Project,Event



def project_list(request):

    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    project = Project.objects.filter(Q(title__icontains=search_query))

    context = {
        "project": project,
        "search_query": search_query,
    }
    return render(request, "list.html", context)


def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("project-list")

    context = {
        "form": form,
    }
    return render(request, "create.html", context)


def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project-list")

    context = {
        "project": project,
        "form": form,
    }
    return render(request, "edit.html", context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("project-list")

    context = {
        "project": project,
    }
    return render(request, "delete.html", context)

def event_list(request):
    event = Event.objects.all()
    context = {
        "event": event,
    }
    return render(request, "event.html", context)


def create_event(request):
    form = EventForm()

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event-list")

    context = {
        "form": form,
    }
    return render(request, "event.html", context)


def edit_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=evemt)
        if form.is_valid():
            form.save()
            return redirect("event-list")

    context = {
        "evemt": event,
        "form": form,
    }
    return render(request, "event.html", context)


def delete_event(request, pk):
    event = Event.objects.get(id=pk)

    if request.method == "POST":
        event.delete()
        return redirect("event-list")

    context = {
        "event": event,
    }
    return render(request, "event.html", context)
