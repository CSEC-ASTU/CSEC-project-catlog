import json
import logging

# fmt: off
from authentication.models import User
from companies.models import Company
# import django Login Require mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
    extra_context = {"page": "all-project"}

    def get_queryset(self):
        search = self.request.GET.get("search", None)
        status = self.request.GET.get("status", None)
        queryset = Project.objects.filter(is_deleted=0)

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        # Status filter for all project endpoint is only allowed for admins
        if self.request.user.is_staff:
            if status:
                queryset = queryset.filter(status__iexact=status)

            return queryset.order_by("-created_at")

        return queryset.order_by("status", "-created_at")


class ProjectDetails(DetailView):
    model = Project
    template_name = "dashboard/project-details.html"
    context_object_name = "project"


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


class ProjectApproval(DetailView):
    model = Project
    template_name = "dashboard/project-approval.html"
    context_object_name = "project"
    http_method_names = ["post"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return JsonResponse(
                {"error": "You are not authorized to perform this action."}
            )

        project = self.get_object()
        status = request.POST.get("status", None)

        if status == "approved":
            project.approved_at = timezone.now()
            project.approved_by = request.user
            project.is_approved = True
            project.status = "approved"
            project.save()
            return JsonResponse(
                {"success": "Project has been approved.", "error": False}, status=200
            )
        elif status == "rejected":
            project.rejected_at = timezone.now()
            project.rejected_by = request.user
            project.is_approved = False
            project.status = "rejected"
            project.save()
            return JsonResponse(
                {"success": "Project has been rejected.", "error": False}, status=200
            )
        else:
            return JsonResponse({"error": "Invalid status."}, status=400)


class ProjectRating(DetailView):
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

        if not request.user.is_authenticated:
            return JsonResponse(
                {"error": "You are not authorized to perform this action."}, status=400
            )

        if not rating.isdigit():
            return JsonResponse({"error": "Rating must be a number"}, status=400)

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
    extra_context = {"page": "my-project"}

    def get_queryset(self):
        search = self.request.GET.get("search", None)
        status = self.request.GET.get("status", None)
        queryset = Project.objects.filter(is_deleted=0, user=self.request.user)

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        if status:
            queryset = queryset.filter(status__iexact=status)

        return queryset.order_by("status", "-created_at")


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
