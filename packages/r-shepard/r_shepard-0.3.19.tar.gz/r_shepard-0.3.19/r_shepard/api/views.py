import os
from typing import Any

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView, View
from two_factor.views.mixins import OTPRequiredMixin

from .models import Container, Project
from .podman import (
    PodmanError,
    is_container_running,
    remove_container,
    start_container,
    stop_container,
)


class ProjectListView(OTPRequiredMixin, ListView):
    model = Project
    template_name = "project_list.html"
    context_object_name = "projects"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Add accumulated resource usage to the context."""
        context = super().get_context_data(**kwargs)
        context["cpu_available"] = os.cpu_count()
        context["ram_available"] = round(
            os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / (1024**3), 2
        )
        context["cpu_allocated_to_projects"] = sum(
            project.max_cpus for project in Project.objects.all()
        )
        context["ram_allocated_to_projects"] = sum(
            project.max_ram for project in Project.objects.all()
        )
        context["cpu_allocated_to_running_containers"] = sum(
            container.cpus
            for project in Project.objects.all()
            for container in project.containers.all()
            if container.is_running
        )
        context["ram_allocated_to_running_containers"] = sum(
            container.ram
            for project in Project.objects.all()
            for container in project.containers.all()
            if container.is_running
        )

        context["ratio_running_containers_to_available_cpu"] = (
            context["cpu_allocated_to_running_containers"]
            / context["cpu_available"]
            * 100
        )
        context["ratio_projects_to_available_cpu"] = (
            context["cpu_allocated_to_projects"] / context["cpu_available"] * 100
        )

        context["ratio_projects_to_available_ram"] = (
            context["ram_allocated_to_projects"] / context["ram_available"] * 100
        )
        context["ratio_running_containers_to_available_ram"] = (
            context["ram_allocated_to_running_containers"]
            / context["ram_available"]
            * 100
        )

        return context


class ProjectDetailView(OTPRequiredMixin, DetailView):
    model = Project
    template_name = "project_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        pass

    def stop_all_project_containers(self):
        # Logic to stop all podman containers for the project
        pass

    context_object_name = "project"


class CreateContainerView(View):
    def post(self, request, *args, **kwargs):
        # Initialize message HTML
        message_html = render_to_string("messages.html")

        # Get project from URL
        project = Project.objects.get(pk=self.kwargs["project_pk"])

        # Get values from the form
        password = request.POST.get("password")
        ram = int(request.POST.get("ram"))
        cpus = int(request.POST.get("cpus"))
        tag = str(request.POST.get("tag"))

        # Set default tag if not provided
        tag = tag or "latest"

        # Calculate total resources used by all containers of the project
        total_ram = sum(container.ram for container in project.containers.all())
        total_cpus = sum(container.cpus for container in project.containers.all())

        # Check if the project has enough resources
        if len(project.containers.all()) >= project.max_containers:
            messages.error(request, "Maximum number of containers reached.")
            message_html = render_to_string(
                "messages.html", {"messages": messages.get_messages(request)}
            )
        elif total_ram + ram > project.max_ram or total_cpus + cpus > project.max_cpus:
            messages.error(request, "Not enough resources for this action.")
            message_html = render_to_string(
                "messages.html", {"messages": messages.get_messages(request)}
            )
        else:
            # Create container instance with project and password if all checks pass
            container = Container.objects.create(
                project=project, tag=tag, password=password, ram=ram, cpus=cpus
            )

            # Start podman container
            try:
                start_container(project, container, password)
                container.is_running = True
                container.save()
            except PodmanError as e:
                container.delete()
                messages.error(request, str(e))
                message_html = render_to_string(
                    "messages.html", {"messages": messages.get_messages(request)}
                )

        # Render the container list template with the updated project
        container_list_html = render_to_string(
            "container_list.html", {"project": project}
        )

        return HttpResponse(container_list_html + message_html)


class StartContainerView(OTPRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Initialize message HTML
        message_html = render_to_string("messages.html")

        # Get project and container from URL
        project = get_object_or_404(Project, pk=kwargs["project_pk"])
        container = get_object_or_404(Container, pk=kwargs["container_pk"])

        # Start container if it is not running
        try:
            if not is_container_running(project, container):
                start_container(project, container)
        except PodmanError as e:
            messages.error(request, str(e))
            message_html = render_to_string(
                "messages.html", {"messages": messages.get_messages(request)}
            )

        # Update container status in the database
        container.is_running = True
        container.save()

        # Render the container list template with the updated project
        container_list_html = render_to_string(
            "container_list.html", {"project": project}
        )

        return HttpResponse(container_list_html + message_html)


class StopContainerView(OTPRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Initialize message HTML
        message_html = render_to_string("messages.html")

        # Get project and container from URL
        project = get_object_or_404(Project, pk=kwargs["project_pk"])
        container = get_object_or_404(Container, pk=kwargs["container_pk"])

        # Stop container if it is running
        try:
            if is_container_running(project, container):
                stop_container(project, container)
        except PodmanError as e:
            messages.error(request, str(e))
            message_html = render_to_string(
                "messages.html", {"messages": messages.get_messages(request)}
            )

        # Update container status in the database
        container.is_running = False
        container.save()

        # Render the container list template with the updated project
        container_list_html = render_to_string(
            "container_list.html", {"project": project}
        )

        return HttpResponse(container_list_html + message_html)


class DeleteContainerView(OTPRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Initialize message HTML
        message_html = render_to_string("messages.html")

        # Get project and container from URL
        project = get_object_or_404(Project, pk=kwargs["project_pk"])
        container = get_object_or_404(Container, pk=kwargs["container_pk"])

        # Remove container if it is running
        try:
            if is_container_running(project, container):
                remove_container(project, container)
        except PodmanError as e:
            messages.error(request, str(e))
            message_html = render_to_string(
                "messages.html", {"messages": messages.get_messages(request)}
            )

        # Delete container in the database
        container.delete()

        # Render the container list template with the updated project
        container_list_html = render_to_string(
            "container_list.html", {"project": project}
        )

        return HttpResponse(container_list_html + message_html)
