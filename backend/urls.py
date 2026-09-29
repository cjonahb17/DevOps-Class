from django.http import JsonResponse
from django.urls import path

def home(request):
    return JsonResponse({
        "message": "Hello from Django!",
        "status": "Backend is working"
    })

urlpatterns = [
    path("", home),
]
