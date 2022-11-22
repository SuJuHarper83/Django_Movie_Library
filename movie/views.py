from django.shortcuts import render
from django.http import Http404
from serializers import MovieSerializer
from rest_framework.decorators import APIView
from rest_framework import Response
from rest_framework import status

# Create your views here.

class MovieList(APIView):

    def get(self, request):
        pass

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)