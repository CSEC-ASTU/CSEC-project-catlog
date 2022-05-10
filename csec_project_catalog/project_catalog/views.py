from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import ListView
# import django Login Require mixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProjectForm, EventForm
from .models import Project, Event
from authentication.models import User

class DashboardView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'dashboard/index.html'
    context_object_name = 'projects'

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['total_project'] = Project.objects.filter(
            is_deleted=0, is_approved=1).count()
        kwargs['total_talents'] = User.objects.filter(is_deleted=0).count()
        kwargs['total_companies'] = 10
        kwargs['recent_projects'] = Project.objects.filter(
            is_deleted=0, is_approved=1).order_by('-created_at')[:5]
        kwargs['your_recente_projects'] = Project.objects.filter(
            is_deleted=0, user=self.request.user).order_by('-created_at')[:5]
        return super().get_context_data(**kwargs)


def project_list(request):

    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    projects = Project.objects.filter(Q(title__icontains=search_query))

    context = {
        "projects": projects,
        "search_query": search_query,
    }
    return render(request, "dashboard/project-list.html", context)

class MyProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'dashboard/my-project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

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
