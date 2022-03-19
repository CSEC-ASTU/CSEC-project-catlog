from django import forms
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        
        fields = ('title', 'description', 'project_link', 'github_link',)

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'project_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Project link'}),
            'github_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Github link'}),
        }