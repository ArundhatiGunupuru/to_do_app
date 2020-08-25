from django.urls import path, include
from . import views
from .views import (TaskListView,
                    TaskCreateView,
                    TodayTaskCreateView,
                    TaskCompleteView,
                    TaskUpdateView,
                    TaskDeleteView)

urlpatterns = [
    path('', TaskListView.as_view(), name='week-tasks'),
    path('task/', TaskListView.as_view(template_name='tasks/job_list_today.html'), name='today-tasks'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/new/today/', TodayTaskCreateView.as_view(), name='task-create2'),
    path('task/<int:pk>/', include([
        path('move_to_today/', views.move_to_today, name='task-move-to-today'),
        path('move_to_week/', views.move_to_week, name='task-move-to-week'),
        path('update/', TaskUpdateView.as_view(), name='task-update'),
        path('delete/', TaskDeleteView.as_view(), name='task-delete'),
        path('complete/', TaskCompleteView.as_view(), name='task-complete'),
    ])),
]

# remove redundancy on the last
#path('delete/<str:week>/', TaskDeleteView.as_view(), name='task-delete'),
#path('delete/<str:today>/', TodayTaskDeleteView.as_view(), name='task-delete2'),
""" removed
# path('task/', TodayTaskListView.as_view(), name='today-tasks'), template_name = 'tasks/job_list_today.html'
#path('update/today/', TodayTaskUpdateView.as_view(), name='task-update2'),
                    # TodayTaskListView,
                    # TodayTaskUpdateView,
changed the code to remove extra list and update view for today and
instead added logic use the same view for both week and today...
"""
