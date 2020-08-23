from django import forms
from .models import Job


class WeekTaskForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title']
