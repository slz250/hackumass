from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html_response = "<h1>Welome to Voice Analysis</h1>"
    return HttpResponse(html_response)

