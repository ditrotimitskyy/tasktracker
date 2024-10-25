from django.urls import path
from .views import TaskView

urlpatterns = [
    path("list/", TaskView.as_view
]