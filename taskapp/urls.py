from django.urls import path

from .views import TaskListView, TaskDetailView,TaskCreateView,TaskUpdateView, TaskDeleteView, CommentUpdateView

urlpatterns = [
    path("list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>" ,TaskDetailView.as_view(),name="task-detail"),
    path("task/new/",TaskCreateView.as_view(),name="create-task"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task-update" ),
    path("task/delete/<int:pk>", TaskDeleteView.as_view(), name='task-delete'),
    path("comment/update/<int:pk>", CommentUpdateView.as_view(), name='comment-update')
]