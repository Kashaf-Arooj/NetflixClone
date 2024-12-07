from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse
from django.core.paginator import Paginator
#________________________________________________________________ Movie _________________________________________________________________________
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    parser_classes = (MultiPartParser, FormParser)


    def list(self, request, *args, **kwargs):
        # Retrieve query parameters
        title = request.GET.get('title', None)
        movie_type = request.GET.get('type', None)
        limit = request.GET.get('limit', 10)  # Default to 10 if not provided
        offset = request.GET.get('offset', 0)  # Default to 0 if not provided

        # Convert limit and offset to integers
        try:
            limit = int(limit)
            offset = int(offset)
        except ValueError:
            return Response({'error': 'Invalid limit or offset parameter'}, status=400)

        # Filter movies by type and title if provided
        filter_kwargs = {}
        if movie_type:
            filter_kwargs['type'] = movie_type
        if title:
            filter_kwargs['title__icontains'] = title

        movies = Movie.objects.filter(**filter_kwargs)

        # Apply pagination
        paginator = Paginator(movies, limit)
        page_number = (offset // limit) + 1
        page = paginator.get_page(page_number)

        # Serialize the data
        serializer = self.get_serializer(page.object_list, many=True)

        # Prepare response data
        response_data = {
            'count': paginator.count,
            'next': page.has_next() and self.get_next_link(request, movie_type, limit, offset, title) or None,
            'previous': page.has_previous() and self.get_previous_link(request, movie_type, limit, offset, title) or None,
            'results': serializer.data,
        }

        return Response(response_data)

    def get_next_link(self, request, movie_type, limit, offset, title):
        next_offset = offset + limit
        return request.build_absolute_uri(f"/api/movies/?type={movie_type}&title={title}&limit={limit}&offset={next_offset}")

    def get_previous_link(self, request, movie_type, limit, offset, title):
        prev_offset = max(0, offset - limit)
        return request.build_absolute_uri(f"/api/movies/?type={movie_type}&title={title}&limit={limit}&offset={prev_offset}")

    