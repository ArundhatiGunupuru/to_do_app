# Job model having fields - title, content, task_for_today
# 'get_absolute_url' - checks for "task_for_today" field and return the url accordingly.


from django.db import models
from django.shortcuts import reverse


class Job(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    task_for_today = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.task_for_today:
            return reverse('today-tasks')
        else:
            return reverse('week-tasks')
