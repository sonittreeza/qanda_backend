from django.urls import path
from .views import *
from api import views


urlpatterns = [
    path('tasklist/', views.TaskListCreateView.as_view(), name='tasklist'),
    path('tasklist/<int:pk>/',views.TaskRetrieveUpdateDestroyView.as_view(), name='tasklist_detail'),


]
