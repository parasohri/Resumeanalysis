from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
def health_check(request):
    return JsonResponse({
        "status": "OK",
        "message": "Backend is running"
    })

urlpatterns = [
    path("", health_check),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('resume.urls')),
]
