from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.shortcuts import render
import json

from .models import Contact, HomePage, Service, Project


# =========================
# HOME PAGE
# =========================
def home(request):

    homepage = HomePage.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {
        'homepage': homepage,
        'services': services,
        'projects': projects,
    })


# =========================
# ABOUT PAGE
# =========================
def about(request):
    return render(request, 'about.html')


# =========================
# SERVICES PAGE
# =========================
def services(request):

    services = Service.objects.all()

    return render(request, 'services.html', {
        'services': services,
    })


# =========================
# PROJECTS PAGE
# =========================
def projects(request):

    projects = Project.objects.all()

    return render(request, 'projects.html', {
        'projects': projects,
    })


# =========================
# CONTACT PAGE
# =========================
def contact_page(request):
    return render(request, 'contact.html')


# =========================
# CONTACT API
# =========================
@csrf_exempt
def contact(request):

    print("VIEW HIT")
    print("METHOD:", request.method)

    if request.method == "POST":

        try:
            data = json.loads(request.body)

            name = data.get("name")
            email = data.get("email")
            message = data.get("message")

            # Save to database
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Email to user
            #send_mail(
             #   subject="Thank You for Contacting Kiwa Energy Solutions",
              #  message=(
               #     f"Hello {name},\n\n"
                #    "Thank you for contacting Kiwa Energy Solutions.\n"
                 #   "We have received your message and will respond shortly.\n\n"
                  #  "Best regards,\n"
                   # "Kiwa Energy Team"
                #),
                #from_email="kiwagreenergy@gmail.com",
                #recipient_list=[email],
                #fail_silently=False,
            #)

            # Email to business owner
            #send_mail(
             #   subject=f"New Inquiry from {name}",
              #  message=(
               #     f"Name: {name}\n"
                #    f"Email: {email}\n\n"
                 #   f"Message:\n{message}"
                #),
                #from_email="kiwagreenergy@gmail.com",
                #recipient_list=["kiwagreenergy@gmail.com"],
                #fail_silently=False,
            #)

            send_mail(
    subject="SMTP Test",
    message="Testing Render SMTP",
    from_email="kiwagreenergy@gmail.com",
    recipient_list=["kiwagreenergy@gmail.com"],
    fail_silently=False,
)

            return JsonResponse({
                "message": "Message sent successfully"
            })

        except Exception as e:

            print("ERROR:", repr(e))
            

            return JsonResponse({
                "message": str(e)
            }, status=500)

    return JsonResponse({
        "error": "Invalid request"
    })