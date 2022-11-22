from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class MovieList(APIView):

    def get(self, request):
        director_param = request.query_params.get('director')
        genre_param = request.query_params.get('genre')
        movies = Movie.objects.all()
        if director_param:
            movies = movies.filter(director=director_param)
        serializer = MovieSerializer(movies, many=True)
        if genre_param:
            movies = movies.filter(genre=genre_param)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MovieDetail(APIView):

    def get(self, request, pk):
       requested_movie = get_object_or_404(Movie, pk=pk)
       serializer = MovieSerializer(requested_movie)
       return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        requested_movie = get_object_or_404(Movie, pk=pk)
        requested_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MoviesCustom(APIView):

    def get(self, request):
        horror_movies = Movie.objects.filter(genre='Horror')
        action_movies = Movie.objects.filter(genre='Action')

        horror_serializer = MovieSerializer(horror_movies, many=True)
        action_serializer = MovieSerializer(action_movies, many=True)

        custom_response_dictionary = {
            "Horror": horror_serializer.data,
            "Action": action_serializer.data,
        }
        return Response(custom_response_dictionary)

