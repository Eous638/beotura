from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlaceSerializer, CategorySerializer, TourSerializer
from .models import Place, Tour, Category
# Create your views here.

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('ordering')
    serializer_class = PlaceSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer