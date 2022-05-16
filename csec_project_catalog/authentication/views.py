from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView, UpdateView

from .forms import UserRegistrationForm
from .models import User


def registeration(request):
    if request.method == "POST":
        print(request.POST)
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.is_active = False
            new_user.save()

            return render(
                request, "authentication/register_done.html", {"new_user": new_user}
            )
        else:
            print(user_form.errors)

    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/register.html", {"user_form": user_form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "dashboard/user_profile.html"

    def get_object(self):
        return self.request.user


class ProfileEditView(LoginRequiredMixin, TemplateView):
    template_name = "authentication/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        print("POST", request.POST)
        self.object = self.get_object()
        user = self.object

        if "first_name" in request.POST:
            user.first_name = request.POST["first_name"]
        if "last_name" in request.POST:
            user.last_name = request.POST["last_name"]
        if "phone_number" in request.POST:
            user.phone_number = request.POST["phone_number"]
        if "birth_date" in request.POST:
            user.birthdate = request.POST["birth_date"]
        else:
            print("birthdate not in request.POST", request.POST.get("birthdate", None))
        if "gender" in request.POST:
            user.gender = request.POST["gender"]

        user.save()

        return self.render_to_response(self.get_context_data(**kwargs))
