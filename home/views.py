from django.shortcuts import render, HttpResponse, redirect
from datetime import date
from django.core.mail import send_mail
from django.contrib import messages
from .models import Home

# Create your views here.

def my_view(request):
    today = date.today()  # Get today's date
    return render(request, 'your_template.html', {'today': today})

def home(request):
    return render(request, 'home.html')

def project(request):
    return render(request, 'project.html')

def project_index(request):
    return render(request, 'project_index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not subject or not message:
            messages.error(request, "All fields are required.")
            return redirect("contact")  # Redirect to avoid saving empty data
        
        # Save to the database
        contact = Home(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Process form (e.g., send email)
        try:
            send_mail(
                subject,
                message,
                "noreply@example.com",
                ["admin@example.com"],
                fail_silently=False  # Set to False for debugging
            )
            messages.success(request, "Your message has been sent!")
        except Exception as e:
            messages.error(request, f"Error sending email: {str(e)}")

        return redirect("contact")  # Redirect after success

    return render(request, 'contact.html')

def skills(request):
    return render(request, 'skills.html')
