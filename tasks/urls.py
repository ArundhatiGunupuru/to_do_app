from django.urls import path, include
from . import views
from .views import (TaskListView,
                    TodayTaskListView,
                    TaskCreateView,
                    TodayTaskCreateView,
                    TaskCompleteView,
                    TodayTaskUpdateView,
                    TaskUpdateView,
                    TaskDeleteView)

urlpatterns = [
    path('', TaskListView.as_view(), name='week-tasks'),
    path('task/', TodayTaskListView.as_view(), name='today-tasks'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/new/today/', TodayTaskCreateView.as_view(), name='task-create2'),
    path('task/<int:pk>/', include([
        path('move_to_today/', views.TodayTask, name='task-move-to-today'),
        path('move_to_week/', views.WeekTask, name='task-move-to-week'),
        path('update/', TaskUpdateView.as_view(), name='task-update'),
        path('update/today/', TodayTaskUpdateView.as_view(), name='task-update2'),
        path('delete/', TaskDeleteView.as_view(), name='task-delete'),
        path('complete/', TaskCompleteView.as_view(), name='task-complete'),
    ])),
]


# remove redundancy on the last
#path('delete/<str:week>/', TaskDeleteView.as_view(), name='task-delete'),
#path('delete/<str:today>/', TodayTaskDeleteView.as_view(), name='task-delete2'),
