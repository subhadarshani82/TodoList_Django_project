"""
URL configuration for djangoProject_tpdo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_task',views.todo,name='add_task'),
    path('',views.fetch_task,name='fetch_task'),
    path('task_status/<int:id>',views.task_status,name='task_status'),
    path('get_task/<int:id>',views.get_task_for_update,name='get_task'),
    # path('update_task/<int:id>',views.update_task,name='update_task'),

]
