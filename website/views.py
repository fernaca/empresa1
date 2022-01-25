from django.shortcuts import render

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
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
    else:
        return render(request, 'contact.html', {})
