from django.urls import path
from .views import (
   ResumeAnalyzeView,
     
)

urlpatterns = [
    path('resume/upload/',  ResumeAnalyzeView.as_view()),
    
]
