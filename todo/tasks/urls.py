from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path(
        'api/tasks/<int:author>/', views.TaskListView.as_view()
    ),
    path(
        'api/tasks/task/', views.TaskView.as_view({'post': 'create'})
    ),
    path(
        'api/tasks/task/<int:pk>', views.TaskView.as_view(
            {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
        )
    ),

]
