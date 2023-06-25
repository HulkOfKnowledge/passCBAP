from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,"WebInterface/index.html",{})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Build the email message
        subject = f'New contact form submission: {subject}'
        message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]  # Set the recipient email address

        # Send the email
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        success = True

        return render(request, 'WebInterface/contact.html', {'success': success})
    
    return render(request, 'WebInterface/contact.html')

def handle404(request,exception):
    return render(request, 'WebInterface/404.html', {})