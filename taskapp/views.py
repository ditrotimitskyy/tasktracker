from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .mixins import UserIsOwnerMixin
from .models import Task, Comment
from .forms import TaskForm, TaskFilterForm, CommentForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
       
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment: Comment = comment_form.instance
            new_comment.task = self.get_object()
            new_comment.user = request.user
            new_comment.save()

        return redirect(request.path_info)


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

    def get_success_url(self):
        return reverse_lazy("task-detail",  kwargs= {"pk":self.get_object().pk})

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")
    template_name = "taskapp/task_delete.html"



class CommentUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Comment
    template_name = "taskapp/comment_update.html"
    form_class = CommentForm

    def get_success_url(self):
        url = reverse_lazy("task-detail", kwargs={"pk": self.get_object().task.pk})
        return url