from django.urls import path, include
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
    path('task/<int:pk>/', include([
        path('move/', views.TodayTask, name='task-move'),
        path('move2/', views.WeekTask, name='task-move2'),
        path('update/', TaskUpdateView.as_view(), name='task-update'),
        path('update/today/', TodayTaskUpdateView.as_view(), name='task-update2'),
        path('delete/', TaskDeleteView.as_view(), name='task-delete'),
        path('delete/today/', TodayTaskDeleteView.as_view(), name='task-delete2'),
    ])),
]


# remove redundancy on the last
#path('delete/<str:week>/', TaskDeleteView.as_view(), name='task-delete'),
#path('delete/<str:today>/', TodayTaskDeleteView.as_view(), name='task-delete2'),
