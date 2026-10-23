from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signout", views.signout, name="signout"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]