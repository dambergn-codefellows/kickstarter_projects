from django.urls import path
from .views import project_detail_view, projects_list_view

urlpatterns = [
    path('', projects_list_view, name='projects_list'),
    path('<int:pk>', project_detail_view, name='project_detail'),
]