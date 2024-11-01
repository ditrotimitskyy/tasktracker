from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .mixins import UserIsOwnerMixin
from .models import Task
from .forms import TaskForm, TaskFilterForm

class TaskListView(ListView):
    model = Task
    template_name = "taskapp/task_list.html"
    context_object_name = "tasks_list"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "taskapp/create_task.html"
    form_class = TaskForm
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    template_name = "taskapp/create_task.html"
    form_class = TaskForm

    success_url = reverse_lazy("task-list")

    # def get_success_url(self):
    #     return reverse_lazy("task-detail", pk=self.get_object().id)

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")
    template_name = "taskapp/task_delete.html"