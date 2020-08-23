from django.urls import path
from . import views
from .views import (TaskListView,
                    TodayTaskListView,
                    TaskCreateView,
                    TodayTaskCreateView,
                    TodayTaskDeleteView,
                    TodayTaskUpdateView,
                    TaskUpdateView,
                    TaskDeleteView)

urlpatterns = [
    path('', TaskListView.as_view(), name='week-tasks'),
    path('task/', TodayTaskListView.as_view(), name='today-tasks'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/new/today/', TodayTaskCreateView.as_view(), name='task-create2'),
    path('task/<int:pk>/move/', views.TodayTask, name='task-move'),
    path('task/<int:pk>/move2/', views.WeekTask, name='task-move2'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/update/today/', TodayTaskUpdateView.as_view(), name='task-update2'),
    path('task/<int:pk>/delete/today/', TodayTaskDeleteView.as_view(), name='task-delete2'),
]


# remove redundancy on the last
