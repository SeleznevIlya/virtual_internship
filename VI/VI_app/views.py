from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import PerevalSerializer


class PerevalAPIView(APIView):

    def get(self, request):
        pereval_list = PerevalAdded.objects.all().values()
        return Response({'perevals': PerevalSerializer(pereval_list, many=True).data})

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pereval_new = PerevalAdded.objects.create(
            author_id=request.data['author_id'],
            beauty_title=request.data['beauty_title'],
            title=request.data['title'],
            other_title=request.data['other_title'],
            coord_id=request.data['coord_id'],
            areas_id=request.data['areas_id'],
            winter_level_id=request.data['winter_level_id'],
            spring_level_id=request.data['spring_level_id'],
            summer_level_id=request.data['summer_level_id'],
            autumn_level_id=request.data['autumn_level_id'],
        )
        return Response({'pereval': PerevalSerializer(pereval_new).data})


# class PerevalAPIView(generics.ListAPIView):
#     queryset = PerevalAdded.objects.all()
#     serializer_class = PerevalSerializer
