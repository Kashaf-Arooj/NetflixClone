from rest_framework import serializers
from .models import *

#________________________________________________________________ CustomUser __________________________________________________________________  
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'profiles']
#         extra_kwargs = {
#             'profiles': {'required': True},}
        
#________________________________________________________________ Profile __________________________________________________________________  
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['id', 'name', 'age_limit']
#         extra_kwargs = {
#             'name': {'required': True},
#             'age_limit': {'required': True},}
# class MultiImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProImage
#         fields = ["id", "movie", "image"]

# class MovieSerializer(serializers.ModelSerializer):
#     images = MultiImageSerializer(many=True, read_only=True)
#     uploaded_images = serializers.ListField(
#         child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
#         write_only=True
#     )

#     class Meta:
#         model = Movie
#         fields = ['id', 'title','created', 'type', 'trailer_video', 'cover_image',  'uploaded_images', 'director', 'release_date', 'movie_story', 'cast', 'movie_link', 'images',]
#         extra_kwargs = {
#             'title': {'required': True},
#             'movie_story': {'required': True},
#             'created': {'required': True},
#             'type': {'required': True},
#             'trailer_video': {'required': True},
#             'cover_image': {'required': True},
#             'director': {'required': True},
#             'release_date': {'required': True},
#             'cast': {'required': True},
#             'images': {'required': True},
#             'movie_link': {'required': True},
#         }
#     def create(self, validated_data):
#         uploaded_images = validated_data.pop("uploaded_images", [])
#         movie = Movie.objects.create(**validated_data)
#         for image in uploaded_images:
#             ProImage.objects.create(movie=movie, image=image)
#         return movie
            
        
class MultiImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProImage
        fields = ["id", "movie", "image"]

class MovieSerializer(serializers.ModelSerializer):
    images = MultiImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False  # We set this to False so that it's not required in the serializer
    )
    class Meta:
        model = Movie
        fields = ['id', 'title', 'created', 'type', 'trailer_video', 'cover_image', 'uploaded_images', 'director', 'release_date', 'movie_story', 'cast', 'movie_link', 'images']
        extra_kwargs = {
            'title': {'required': True},
            'movie_story': {'required': True},
            'created': {'required': True},
            'type': {'required': True},
            'trailer_video': {'required': True},
            'cover_image': {'required': True},
            'director': {'required': True},
            'release_date': {'required': True},
            'cast': {'required': True},
            'images': {'required': True},
            'movie_link': {'required': True},
        }

    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        movie = Movie.objects.create(**validated_data)
        for image in uploaded_images:
            ProImage.objects.create(movie=movie, image=image)
            movie.save()
        return movie