from django.contrib import admin
from django.urls import path, include
from .views import GoogleAuthView, KakaoAuthView
urlpatterns = [
    path('api/v2/auth/google', GoogleAuthView.as_view()),
    path('api/v2/auth/kakao', KakaoAuthView.as_view())
]
