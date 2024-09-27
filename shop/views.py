from rest_framework import viewsets
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilters
from rest_framework.filters import SearchFilter, OrderingFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilters
    search_fields = ['product_name']
    ordering_fields = ['price', 'date']


class ProductPhotoViewSet(viewsets.ModelViewSet):
    queryset = ProductPhotos.objects.all()
    serializer_class = ProductPhotoSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializers_class = ReviewSerializer