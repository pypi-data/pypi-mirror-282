import os
from typing import Any

from django import forms
from django.contrib import admin, messages
from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse

from .models import Container, Project
from .podman import PodmanError, start_container

admin.site.site_header = "R-Shepard"
admin.site.site_title = "R-Shepard"
admin.site.index_title = "Admin Area"


class EditContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = "__all__"
        # These fields cannot be edited and are excluded from the edit form
        exclude = [
            "project",
            "container_id",
            "password",
            "port",
            "local_url",
            "is_running",
        ]


class AddContainerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Container
        fields = "__all__"
        exclude = [
            "container_id",
            "is_running",
            "port",
            "local_url",
        ]


class ContainerAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request: Any, obj: Any):
        if obj:  # Edit
            return ["project", "container_id"]
        else:  # Add
            return ["container_id", "image", "tag"]

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            return EditContainerForm
        else:
            return AddContainerForm

    # This is only really needed for creating containers from Admin so the logic
    # should correspond to the CreateContainerView
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        # Calculate total resources used by all containers of the project
        total_ram = sum(container.ram for container in obj.project.containers.all())
        total_cpus = sum(container.cpus for container in obj.project.containers.all())

        # Check if the project has enough resources
        if len(obj.project.containers.all()) >= obj.project.max_containers:
            messages.error(request, "Maximum number of containers reached.")
            return
        if (
            total_ram + obj.ram > obj.project.max_ram
            or total_cpus + obj.cpus > obj.project.max_cpus
            or len(obj.project.containers.all()) >= obj.project.max_containers
        ):
            messages.error(request, "Not enough resources.")
            return

        # Start podman container
        try:
            start_container(obj.project, obj, obj.password)
            obj.is_running = True
        except PodmanError as e:
            messages.error(request, str(e))
            return
        super().save_model(request, obj, form, change)

    # Redirect to project detail page after adding a container
    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(reverse("project_detail", args=[obj.project.pk]))

    def response_change(self, request: HttpRequest, obj: Any) -> HttpResponse:
        return HttpResponseRedirect(reverse("project_detail", args=[obj.project.pk]))


class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "max_containers",
            "max_ram",
            "max_cpus",
            "auto_commit_enabled",
            "git_repo_url",
            "commit_interval",
        ]

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        max_ram = cleaned_data.get("max_ram")
        max_cpus = cleaned_data.get("max_cpus")
        if max_ram and max_cpus:
            if max_ram < 0 or max_cpus < 0:
                raise forms.ValidationError("Maximum RAM and CPUs must be positive.")

        system_cpus = os.cpu_count()
        system_ram = (
            os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / (1024.0**3)
        )

        # Exclude the current project from the sums
        other_projects = Project.objects.exclude(id=self.instance.id)

        available_cpus = system_cpus - sum(
            project.max_cpus for project in other_projects
        )
        available_ram = system_ram - sum(project.max_ram for project in other_projects)

        if max_ram > available_ram:
            self.add_error("max_ram", "Not enough RAM available.")
        if max_cpus > available_cpus:
            self.add_error("max_cpus", "Not enough CPUs available.")

        return cleaned_data


class ProjectChangeForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        max_ram = cleaned_data.get("max_ram")
        max_cpus = cleaned_data.get("max_cpus")
        if max_ram and max_cpus:
            if max_ram < 0 or max_cpus < 0:
                raise forms.ValidationError("Maximum RAM and CPUs must be positive.")

        system_cpus = os.cpu_count()
        system_ram = (
            os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / (1024.0**3)
        )

        # Exclude the current project from the sums
        other_projects = Project.objects.exclude(id=self.instance.id)

        available_cpus = system_cpus - sum(
            project.max_cpus for project in other_projects
        )
        available_ram = system_ram - sum(project.max_ram for project in other_projects)

        if max_ram > available_ram:
            self.add_error("max_ram", "Not enough RAM available.")
        if max_cpus > available_cpus:
            self.add_error("max_cpus", "Not enough CPUs available.")

        return cleaned_data


class ProjectAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj:
            return ProjectChangeForm
        else:
            return ProjectAddForm

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(reverse("project_list"))

    def response_change(self, request: HttpRequest, obj: Any) -> HttpResponse:
        return HttpResponseRedirect(reverse("project_detail", args=[obj.pk]))


admin.site.register(Container, ContainerAdmin)
admin.site.register(Project, ProjectAdmin)
