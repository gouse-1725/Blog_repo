from rest_framework import serializers
from . import models

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog_category
        fields = '__all__'

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog_Image
        fields = '__all__'
        read_only_fields = ['blog']  # Assuming blog is set automatically in the view



class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    images = BlogImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Blog
        fields = '__all__'

