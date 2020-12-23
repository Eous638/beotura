from django.urls import path, include
from  django.contrib import admin
from rest_framework.routers import DefaultRouter
from beotura import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Places', views.PlaceViewSet)
router.register(r'Tours', views.TourViewSet)

router.register(r'Categorys', views.CategoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]