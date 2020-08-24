from django.db import models
from django.shortcuts import reverse

# these are the tasks for the entire week


class Job(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    task_for_today = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('week-tasks')

# check if we can use task for tday field and then give the absolute url
