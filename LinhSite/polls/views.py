from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("I'm Hoai Linh 20PFIEV3, now I'm at the polls index. I've finished Lab_1 For DRF!")