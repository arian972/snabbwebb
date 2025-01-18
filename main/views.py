from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')

def projects(request):
    return render(request, 'main/projects.html')