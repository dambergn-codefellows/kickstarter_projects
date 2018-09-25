from django.urls import path
from .views import project_detail_view, projects_list_view

urlpatterns = [
    path('', review_list_view, name='project_list'),
    path('<int:pk>', review_detail_view, name='project_detail')
]