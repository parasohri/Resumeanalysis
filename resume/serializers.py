from rest_framework import serializers

from .models import SavedResumeAnalysis

class ResumeAnalyzeSerializer(serializers.Serializer):
    file = serializers.FileField()
    job_description = serializers.CharField()
    save = serializers.BooleanField(required=False, default=False)

class SavedResumeAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedResumeAnalysis
        fields = [
            "id",
            "job_description",
            "analysis_result",
            "created_at"
        ]