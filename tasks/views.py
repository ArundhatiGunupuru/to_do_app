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


class TodayTaskListView(ListView):
    model = Job
    fields = ['title', 'content']
    context_object_name = 'jobs'
    template_name = 'tasks/job_list_today.html'


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

    def get_success_url(self):
        return reverse('today-tasks')

    # can add variables for 2 functions...

    # def get_success_url(self):
    #    return reverse('book-detail', kwargs={'pk': self.object.pk}

# class TaskDetailView(DetailView):
#    model = Job


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'The task was Updated'


class TodayTaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    fields = ['title', 'content']
    success_message = 'The task was Updated'

    def get_success_url(self):
        return reverse('today-tasks')


class TaskDeleteView(DeleteView):
    model = Job
    success_url = '/'


class TodayTaskDeleteView(DeleteView):
    model = Job

    def get_success_url(self):
        return reverse('today-tasks')


def TodayTask(request, pk):
    Job.objects.filter(id=pk).update(task_for_today=True)
    return redirect('week-tasks')


def WeekTask(request, pk):
    Job.objects.filter(id=pk).update(task_for_today=False)
    return redirect('today-tasks')

# return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

# class TaskDeleteView(DeleteView):
#    model = Job

#    def get_success_url(self, kwargs):
#        if self.kwargs == 'week':
#            return reverse('week-tasks')
#        else:
#            return reverse('today-tasks')
