from django.http import HttpResponse
from django.shortcuts import render
# this function name is main which is similar to the views.main and in views.main it will grab the main.html file
# above two import are necessary for http response and other is to render the html page
def main(request):
    return render(request,'website/main.html')

