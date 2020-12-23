from rest_framework import serializers
from .models import Place, Tour, Category

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('title', 'title_en', 'description','description_en', 'latitude', 'longitude', 'ordering', 'image', 'icon', 'tour', 'category')

class CategorySerializer(serializers.ModelSerializer):
    Place = PlaceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['title','title_en', 'description','description_en', 'image', 'Place']
class TourSerializer(serializers.ModelSerializer):
    Place = PlaceSerializer(many=True, read_only=True)
    class Meta:
        model = Tour
        fields = ['title','title_en', 'description','description_en', 'image', 'Place']
