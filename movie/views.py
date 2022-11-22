from django.shortcuts import render
from django.http import Http404
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MovieList(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)