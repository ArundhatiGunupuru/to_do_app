from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TaskForm
from .models import Job
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


# This view lists all the tasks for today as well as for entire week.
# For today's tasks the 'task_for_today' field is set to true.
# The template for today's task list view has been mentioned in the url -"job_list_today.html" and
# The template for week's task list view being the default name -"job_list.html"
class TaskListView(ListView):
    model = Job
    fields = ['title', 'content']
    context_object_name = 'jobs'


# Creates the tasks for the week.
# the template -"job_form.html" used to add a new task for week.
class WeekTaskCreateView(SuccessMessageMixin, CreateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'New task was created'


# Creates the tasks for today also setting the 'task_for_today' field to true for a valid form.
# the template -"job_form.html" used to add a new task for today.
class TodayTaskCreateView(SuccessMessageMixin, CreateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'New task for today was created'

    def form_valid(self, form):
        form.instance.task_for_today = True
        return super().form_valid(form)


# This method is called when - a task for today is moved to week.
def move_to_week(request, pk):
    Job.objects.filter(id=pk).update(task_for_today=False)
    return redirect('today-tasks')


# This method is called when - a task for week is moved to today.
def move_to_today(request, pk):
    Job.objects.filter(id=pk).update(task_for_today=True)
    return redirect('week-tasks')


# Both today's task and week's task is updated using this view.
# since added logic in models.py to access paths according to 'task_for_today' field.
# Same template -"job_form.html" used to update the tasks which was used to add new tasks."
class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'The task was Updated'


# Week task can be deleted using delete view and
# template - "job_confirm_delete.html"
class TaskDeleteView(DeleteView):
    model = Job
    success_url = '/'


# if any task for today is completed can be deleted using this view and
# template - "job_confirm_delete.html"
class TaskCompleteView(DeleteView):
    model = Job

    def get_success_url(self):
        return reverse('today-tasks')
