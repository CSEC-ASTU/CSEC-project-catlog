# fmt: off
from companies.forms import CompanyForm
from companies.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView,
)

# fmt: on


class CompaniesListView(ListView):
    model = Company
    template_name = "dashboard/companies.html"  # TODO - change the template folder to its own folder
    context_object_name = "companies"
    paginate_by = 1

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)

    def get_context_data(self, **kwargs):
        kwargs["total_companies"] = Company.objects.filter(is_deleted=False).count()
        return super().get_context_data(**kwargs)


class CompanyDetailView(DetailView):
    model = Company
    template_name = "dashboard/company-detail.html"
    context_object_name = "company"

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)


class CompanyDeleteView(LoginRequiredMixin, TemplateView):
    template_name = "companies/company-delete.html"
    context_object_name = "company"
    success_url = reverse_lazy("companies-list")

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            # Permission denied
            return self.handle_no_permission()

        self.object = self.get_queryset().get(pk=kwargs["pk"])
        self.object.delete()
        return JsonResponse({"error": None, "success": True}, status=200)


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "dashboard/company-create.html"  # TODO - change the template folder to its own folder
    form_class = CompanyForm
    context_object_name = "company"
    success_url = reverse_lazy("companies-list")

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            # Permission denied
            return self.handle_no_permission()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("Request user: ", self.request.user)
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = "companies/company-update.html"
    context_object_name = "company"
    success_url = reverse_lazy("companies-list")
    fields = [
        "name",
        "description",
        "address",
        "city",
        "state",
        "phone_number",
        "country",
        "email",
        "website",
        "logo",
        "facebook",
        "twitter",
        "linkedin",
        "instagram",
        "youtube",
    ]

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            # Permission denied
            return self.handle_no_permission()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
