from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import SavedResumeAnalysis
from .serializers import ResumeAnalyzeSerializer
from .utils import extract_text_from_pdf, analyze_resume_with_ai


class ResumeAnalyzeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResumeAnalyzeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        resume_file = serializer.validated_data["file"]
        job_description = serializer.validated_data["job_description"]
        save = serializer.validated_data["save"]

         
        resume_text = extract_text_from_pdf(resume_file)
 
        del resume_file

       
        # analysis = analyze_resume_with_ai(
        #     resume_text=resume_text,
        #     job_description=job_description
        # )

        
        if save:
            SavedResumeAnalysis.objects.create(
                user=request.user,
                job_description=job_description,
                # analysis_result=analysis,
            )

        return Response(
            {
                # "analysis": analysis,
                "saved": save,
                "text": resume_text
                 
            },
            status=status.HTTP_200_OK
        )
