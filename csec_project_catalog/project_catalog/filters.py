from django_filters import CharFilter, FilterSet
from project_catalog.models import Project


class ProjectFilter(FilterSet):
    title = CharFilter(lookup_expr="iexact")
    created_by = CharFilter(lookup_expr="iexact", name="created_by__username")

    class Meta:
        model = Project
        fields = ["title", "created_by"]
