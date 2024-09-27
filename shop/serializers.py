from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = ['image']


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Rating
        fields = ['user', 'stars']


class ReviewSerializer(serializers.ModelSerializer):
    autor = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Review
        fields = ['id', 'autor', 'text', 'parent_review', 'created_date']


class ProductListSerializer(serializers.ModelSerializer):
    product = ProductPhotoSerializer(read_only=True, many=True)
    category = CategorySerializer()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product', 'category', 'price', 'average_rating', 'date']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ratings = RatingSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    product = ProductPhotoSerializer(read_only=True, many=True)
    date = serializers.DateField(format='%d-%m-%Y')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'product', 'product_video', 'active',
                  'date', 'average_rating', 'ratings', 'reviews']

    def get_average_rating(self, obj):
        return obj.get_average_rating()