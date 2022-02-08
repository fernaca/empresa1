from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Posteos
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

# POST
# Home / ListView


class HomePost(ListView):
    queryset = Posteos.objects.order_by('-created_on')  # Negativo para el Sort
# Otra form de ordenar: ordering = ['-created_on']
    model = Posteos
    template_name = 'posts.html'
    paginate_by = 2  # Objetos por página
    context_object_name = 'Posteos'  # Default: object_list

# DetailView


class ArticleDetailView(DetailView):
    model = Posteos
    template_name = 'article_detail.html'
