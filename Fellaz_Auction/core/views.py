from django.shortcuts import render

# Create your views here.
# View function for home of site
def index(request):
    return render(request, "index.html")

# view function for about page
def about(request):
    return render(request, "about.html")

# View function for Contact page
def contact(request):
    return render(request, "contact.html")