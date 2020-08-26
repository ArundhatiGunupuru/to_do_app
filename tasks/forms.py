from django import forms
from .models import Job


class TaskForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title']
