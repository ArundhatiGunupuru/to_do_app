"""tasks-app URL Configuration

The `urlpatterns` list routes URLs to views.
Function views -
    to move a task from today's list to week's list and vice versa
    we used move_to_today and move_to_week function in views.
Class-based views
    same list view with different template names for today's and week's task.
    create, update and delete views for both today's and week's tasks.
    used a single url ans view for updating tasks.
Including another URLconf
    include function has been used to remove redundancy
"""

from django.urls import path, include
from . import views
from .views import (TaskListView,
                    WeekTaskCreateView,
                    TodayTaskCreateView,
                    TaskCompleteView,
                    TaskUpdateView,
                    TaskDeleteView)

urlpatterns = [
    path('', TaskListView.as_view(), name='week-tasks'),
    path('task/', TaskListView.as_view(template_name='tasks/job_list_today.html'), name='today-tasks'),
    path('task/new/week/<int:task_for>/', WeekTaskCreateView.as_view(), name='week-task-create'),
    path('task/new/today/<int:task_for>/', TodayTaskCreateView.as_view(), name='today-task-create'),
    path('task/<int:pk>/', include([
        path('move_to_today/', views.move_to_today, name='task-move-to-today'),
        path('move_to_week/', views.move_to_week, name='task-move-to-week'),
        path('update/', TaskUpdateView.as_view(), name='task-update'),
        path('delete/', TaskDeleteView.as_view(), name='task-delete'),
        path('complete/', TaskCompleteView.as_view(), name='task-complete'),
    ])),
]
