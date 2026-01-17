from rest_framework import serializers

class ResumeAnalyzeSerializer(serializers.Serializer):
    file = serializers.FileField()
    job_description = serializers.CharField()
    save = serializers.BooleanField(required=False, default=False)
