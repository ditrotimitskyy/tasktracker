from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy,reverse

# Create your views here.
class UserCreateView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("task-list")
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        user = form.instance
        login(self.request, user)
        return redirect(reverse("task-list"))
    