from django.urls import path
from .views import ResumeAnalyzeView
from .views import SavedResumeAnalysisListView
urlpatterns = [
    path("resume/upload/", ResumeAnalyzeView.as_view()),
    path("resume/saved/", SavedResumeAnalysisListView.as_view()),
]
