from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm
from .models import User


def registeration(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it 
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.is_active = False
			new_user.save()

			return render(request, 'authentication/register_done.html', {'new_user': new_user})
		
	else:
		user_form = UserRegistrationForm()
	return render(request, 'authentication/register.html', {'user_form': user_form})

@login_required
def profile(request):
	user = request.user
	return render(request, 'authentication/profile.html', {'user': user})