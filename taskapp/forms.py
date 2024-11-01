from django.forms import ModelForm, Form, ChoiceField


from .models import Task

class TaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = ("title", "due_date", "status")


class TaskFilterForm(Form):
    STATUS_CHOICES = {
        "": "All",
        "done": "Done",
        "in_prog": "In Progress",
        "on_pause": "On Pause",
    }
    status = ChoiceField(choices=STATUS_CHOICES, required=False, label="Status")