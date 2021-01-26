from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Main_Office, Regional_Office, Field_Offices

# Create your views here.
def index(request):
    return render(request, 'branches/index.html', {})


def main_datasets(request):
    points = serialize('geojson', Main_Office.objects.all())
    return HttpResponse(points,content_type='json',)


def regional_datasets(request):
    points = serialize('geojson', Regional_Office.objects.all())
    return HttpResponse(points,content_type='json',)


def field_datasets(request):
    points = serialize('geojson', Field_Offices.objects.all())
    return HttpResponse(points,content_type='json',)