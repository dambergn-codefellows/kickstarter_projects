from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project

# Create your views here.


def projects_list_view(request):
    """
    """
    projects = get_list_or_404(Project)
    context = {
        'projects': projects
    }
    return render(request, 'project/project_list.html', context)


def project_detail_view(request, pk=None):
    """
    """
    project = get_object_or_404(Project, pk)
    context = {
        'project': project.id
    }
    return render(request, 'project/project_detail.html', context)

