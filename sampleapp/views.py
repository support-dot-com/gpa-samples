from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.apps import apps

# Create your views here.
def index(request):
  return HttpResponse("Guided Path Apps System")
