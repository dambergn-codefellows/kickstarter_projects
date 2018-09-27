from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import Project

# Create your views here.


def projects_list_view(request):
    """
    """
    projects_query = get_list_or_404(Project)
    paginator = Paginator(projects, 20)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects
    }
    return render(request, 'project/project_list.html', context)


def project_detail_view(request, pk):
    """
    """
    context = {
        'project': get_object_or_404(Project, id=pk)
        # 'project': project.id
    }
    return render(request, 'project/project_detail.html', context)

