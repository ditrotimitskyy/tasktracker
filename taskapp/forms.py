from django.forms import ModelForm, Form, ChoiceField, FileInput


from .models import Task, Comment

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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'comment_pic']
        widgets = {'comment_pic': FileInput()}