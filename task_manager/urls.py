from django.contrib import admin
from django.urls import path
from tasks.views import (
    all_tasks_view,
    tasks_view,
    delete_task_view,
    complete_task_view,
    completed_tasks_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("add-task", tasks_view),
    path("tasks", all_tasks_view),
    path("delete-task/<int:index>", delete_task_view),
    path("complete_task/<int:index>", complete_task_view),
    path("completed_tasks", completed_tasks_view),
]
