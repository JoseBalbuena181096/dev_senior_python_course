from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse('Hello word')

def goodbye_page_view(request):
    return HttpResponse('Goodbye word')