from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact

@csrf_exempt
def contact_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Contact.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            message=data.get('message')
        )

        return JsonResponse({"message": "Saved successfully"})
    
    return JsonResponse({"error": "Invalid request"}, status=400)
from django.shortcuts import render
from .models import HomePage, Service, Project

def home(request):
    homepage = HomePage.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {
        'homepage': homepage,
        'services': services,
        'projects': projects,
    })