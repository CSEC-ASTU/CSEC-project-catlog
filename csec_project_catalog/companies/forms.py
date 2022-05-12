from django.forms import ModelForm

from companies.models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ("is_deleted", "created_at", "updated_at",
                   "deleted_at", "deleted_by", "created_by", 
                   "updated_by")
