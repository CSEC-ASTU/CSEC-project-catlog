# fmt: off
from companies.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)

# fmt: on


class CompaniesListView(ListView):
    model = Company
    template_name = "companies/companies-list.html"
    context_object_name = "companies"

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)


class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/company-detail.html"
    context_object_name = "company"

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = "companies/company-delete.html"
    context_object_name = "company"
    success_url = reverse_lazy("companies-list")

    def get_queryset(self):
        return Company.objects.filter(is_deleted=False)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_staff:
            # Permission denied
            return self.handle_no_permission()


class CreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = "companies/company-create.html"
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
