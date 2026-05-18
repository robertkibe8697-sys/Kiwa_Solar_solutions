from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.mail import send_mail

import json

from .models import Contact, HomePage, Service, Project


@csrf_exempt
def contact_api(request):

    if request.method == "POST":

        data = json.loads(request.body)

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        # Save message to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send thank-you email to user
        send_mail(
            subject="Thank You for Contacting Kiwa Solar Solutions",
            message=(
                "Hello " + name + ",\n\n"
                "Thank you for contacting Kiwa Solar Solutions.\n"
                "We have received your message and will respond shortly.\n\n"
                "Best regards,\n"
                "Kiwa Solar Team"
            ),
            from_email="kiwagreenergy@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )



        return JsonResponse({
            "message": "Saved successfully"
        })

    return JsonResponse({
        "error": "Invalid request"
    }, status=400)


def home(request):

    homepage = HomePage.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {
        'homepage': homepage,
        'services': services,
        'projects': projects,
    })