from django.urls import path
from . import views

urlpattern = {
    path('', views.MoviesList.as_view()),
}