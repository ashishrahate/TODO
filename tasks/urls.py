from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="Home"),
    path('update_task/<str:pk>', views.update_task, name="Update_task"),
    path('delete_task/<str:pk>', views.delete_task, name="Delete_task")

]