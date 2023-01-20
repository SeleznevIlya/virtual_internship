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
        serializer.save()
        return Response({'pereval': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Method PUT not allowed"})

        try:
            instance = PerevalAdded.objects.get(pk=pk)
        except:
            return Response({'error': "Object does not exist"})

        serializer = PerevalSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'pereval': serializer.data})


# class PerevalAPIView(generics.ListAPIView):
#     queryset = PerevalAdded.objects.all()
#     serializer_class = PerevalSerializer
