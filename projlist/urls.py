from django.contrib import admin
from django.urls import path, include
from projlist.views import ProjectBoardView

urlpatterns = [
    path('', ProjectBoardView.as_view()),
]
