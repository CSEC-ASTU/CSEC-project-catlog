from django.apps import AppConfig


class ProjectCatalogAppConfig(AppConfig):
    name = "project_catalog"
    def ready(self) -> None:
        import project_catalog.signals