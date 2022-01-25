from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def product(request):
    return render(request, 'single-product.html', {})


def about(request):
    return render(request, 'about.html', {})


def products(request):
    return render(request, 'products.html', {})


def contact(request):
    if request.method == 'POST':
        # Capturamos los campos
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # Enviamos el mensaje
        send_mail(
            'Se contactaron desde el sitio',  # Subject
            message,  # Message
            email,  # From Email
            ['fernando.caceres@gmail.com', 'otroemail@gmail.com'],  # To Email
        )
        return render(request, 'contact.html', {'message_name': name})
    else:
        return render(request, 'contact.html', {})
