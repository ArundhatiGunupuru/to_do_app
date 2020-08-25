from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import WeekTaskForm
from .models import Job
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class TaskListView(ListView):
    model = Job
    fields = ['title', 'content']
    context_object_name = 'jobs'

# still an error while creating the task it doesn't set task for today so go back goes to week task
# tried sending a parameter from url to view to reduce it to one view..
# can add variables for 2 functions...
# add comments to all..


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'New task was created'


class TodayTaskCreateView(SuccessMessageMixin, CreateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'New task for today was created'

    def form_valid(self, form):
        form.instance.task_for_today = True
        return super().form_valid(form)


def move_to_week(request, pk):
    Job.objects.filter(id=pk).update(task_for_today=False)
    return redirect('today-tasks')


def move_to_today(request, pk):
    Job.objects.filter(id=pk).update(task_for_today=True)
    return redirect('week-tasks')


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'The task was Updated'


class TaskDeleteView(DeleteView):
    model = Job
    success_url = '/'


class TaskCompleteView(DeleteView):
    model = Job

    def get_success_url(self):
        return reverse('today-tasks')
# the message is wrong for complete task check it in template

#---------------------
# return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

# class TaskDeleteView(DeleteView):
#    model = Job

#    def get_success_url(self, kwargs):
#        if self.kwargs == 'week':
#            return reverse('week-tasks')
#        else:
#            return reverse('today-tasks')


#    def get_success_url(self):
#        if Job.objects.filter(id=pk).task_for_today == True:
#            success_message = 'The task was deleted in today task'
#            return reverse('week-tasks')
#        else:
#            success_message = 'The task was deleted in week task'
#            return reverse('today-tasks')


# changed object to Job in template
"""

    def get_object(self):
        task_for = self.kwargs['task_for']
        if task_for == 1:
            def get_success_url(self):
                return reverse('today-tasks')
        else:
            success_message = 'New task was created and was stored as false'
"""

"""
class TodayTaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'The task was Updated for today'

#    def get_success_url(self):
#        return reverse('today-tasks')
"""
# changed job to Job in template check it -- didn't work so gave object instead

"""
class TaskDetailView(DetailView):
    model = Job

    def get_success_url(self):
        return reverse('book-detail', kwargs={'pk': self.object.pk}
"""

"""
class TodayTaskListView(ListView):
    model = Job
    fields = ['title', 'content']
    context_object_name = 'jobs'
    template_name = 'tasks/job_list_today.html'
"""
# check if template name is given in url will it work with same view

#    def get_success_url(self):
#        return reverse('today-tasks') -  create for today
