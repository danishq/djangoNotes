from django.shortcuts import render

# Create your views here.
def A_app(request):
    return render(request, 'djangoApp/A_app.html')

def tailwindSetup(request):
    return render(request, 'djangoApp/tailwindSetup.html')