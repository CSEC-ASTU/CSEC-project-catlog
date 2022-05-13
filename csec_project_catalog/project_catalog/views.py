import json
import logging

from authentication.models import User
from companies.models import Company
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# fmt: off
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import EventForm, ProjectForm, ProjectImageForm
from .models import Event, Project, Rating

# fmt: on

# add logging to the file
logger = logging.getLogger(__name__)


class DashboardView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "dashboard/index.html"
    context_object_name = "projects"

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["total_project"] = Project.objects.filter(
            is_deleted=0, is_approved=1
        ).count()
        kwargs["total_talents"] = User.objects.filter(is_deleted=0).count()
        kwargs["total_companies"] = Company.objects.filter(is_deleted=0).count()
        kwargs["recent_projects"] = Project.objects.filter(
            is_deleted=0, is_approved=1
        ).order_by("-created_at")[:5]
        kwargs["recently_added_companies"] = Company.objects.filter(
            is_deleted=0
        ).order_by("-created_at")[:5]

        kwargs["your_recente_projects"] = Project.objects.filter(
            is_deleted=0, user=self.request.user
        ).order_by("-created_at")[:5]
        return super().get_context_data(**kwargs)


class ProjectListView(ListView):
    model = Project
    # TODO #20 - change the template folder to its own folder
    template_name = "dashboard/project-list.html"
    context_object_name = "projects"
    paginate_by = 10
    filter_fields = ("title",)
    search_fields = ("title",)

    def get_queryset(self):
        search = self.request.GET.get("search", None)
        queryset = Project.objects.filter(is_deleted=0)
        if self.request.user.is_staff:
            if search:
                # TODO #22 #21 - add filter for the project status(approved, rejected, pending)
                return queryset.filter(
                    Q(title__icontains=search) | Q(description__icontains=search)
                ).order_by("-created_at")

            return queryset

        if search:
            # TODO - add filter for the project status(approved, rejected, pending)
            return (
                queryset.filter(
                    Q(title__icontains=search) | Q(description__icontains=search)
                )
                .filter(is_approved=1)
                .order_by("-created_at")
            )

        return Project.objects.filter(is_deleted=0, is_approved=1)


class ProjectDetails(DetailView):
    model = Project
    template_name = "dashboard/project-details.html"
    context_object_name = "project"

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        if request.user.is_staff:
            project.is_approved = True
            project.save()
            return redirect("project-list")
        else:
            project.status = "declined"
            project.save()
            return redirect("project-list")


@staff_member_required
def project_approve(request, pk):
    project = get_object_or_404(Project, id=pk)
    project.is_approved = True
    project.status = "accepted"
    project.approved_by = request.user
    project.save()
    return redirect("project-list")


@staff_member_required
def project_decline(request, pk):
    project = get_object_or_404(Project, id=pk)
    project.is_approved = False
    project.status = "declined"
    project.is_deleted = True
    project.save()
    return redirect("project-list")


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "dashboard/create-project.html"
    success_url = reverse_lazy("project-list")

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        instance = form.save()
        if "images" in self.request.POST:
            try:
                images = json.loads(self.request.POST["images"])
                instance.images.add(*images)
            except Exception as e:
                logger.exception(e)

        return super().form_valid(form)


class AdminProjectView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "dashboard/admin-project.html"
    context_object_name = "projects"
    paginate_by = 10
    filter_fields = ("title",)
    search_fields = ("title",)

    def get_queryset(self):
        search = self.request.GET.get("search", None)
        queryset = Project.objects.filter(is_deleted=0)
        if search:
            return queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            ).order_by("-created_at")

        return Project.objects.filter(is_deleted=0)


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


class ProjectRating(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "dashboard/project-rating.html"
    context_object_name = "project"
    http_method_names = ["post"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        print("request.POST", request.POST)
        rating = request.POST.get("rating")
        if not rating.isdigit():
            return JsonResponse({"error": "Rating must be a number"})

        if project.rating:
            previous_rating = project.rating.filter(created_by=request.user).first()
            if previous_rating:
                previous_rating.rating = rating
                previous_rating.save()
                return JsonResponse({"success": "Rating added successfully"})

        rating = Rating.objects.create(rating=rating, created_by=request.user)
        project.rating.add(rating)
        return JsonResponse({"success": "Rating added successfully"})


class MyProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "dashboard/project-list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)


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


class DeleteProject(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/project-delete.html"
    http_method_names = ["delete", "post"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = Project.objects.filter(id=pk, is_deleted=0)
        else:
            self.object = Project.objects.filter(
                id=pk, user=self.request.user, is_deleted=0
            )

        if not self.object.exists():
            return JsonResponse(
                {"error": "Project doesn't exist", "success": False}, status=400
            )

        self.object.first().delete()
        return JsonResponse({"error": None, "success": True}, status=200)

    def post(self, request, pk, *args, **kwargs):
        return self.delete(request, pk, *args, **kwargs)


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
        form = EventForm(request.POST, request.FILES, instance=event)
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


class ProjectImageUpload(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/project-image-create.html"
    http_method_names = ["post"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # add created_by to the current user
    def post(self, request, *args, **kwargs):
        form = ProjectImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.created_by = self.request.user
            form.save()

            return JsonResponse(
                {
                    "success": "Image added successfully",
                    "image_id": form.instance.id,
                }
            )

        print(form.errors)

        return JsonResponse({"error": "Image not added successfully"}, status=400)
