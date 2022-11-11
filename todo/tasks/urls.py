from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path(
        'api/tasks/<int:author>/', views.TaskListView.as_view()
    ),
]
