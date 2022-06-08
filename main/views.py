from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from main.serializers import *
import random

from main.models import *


# Create your views here.


class FakeNewsAPIListCreate(generics.ListCreateAPIView):
    queryset = FakeNews.objects.all()
    serializer_class = FakeNewsSerializer

    def get_queryset(self):
        return FakeNews.objects.all()

    def post(self, request, *args, **kwargs):
        answer = True  # что вернет ml
        correct = random.randint(1, 100)  # что вернет ml
        try:
            if request.data['description'] != '' and len(request.data['description']) > 25:
                news = FakeNews.objects.create(description=request.data['description'],
                                               answer=answer,
                                               correct=correct)
                return Response({'news': model_to_dict(news)})
            elif request.data['description'] != '' and len(request.data['description']) < 25:
                return Response({'Error': 'Too short news'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'Error': 'Empty string'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error': 'Error in response(description is required)'}, status=status.HTTP_400_BAD_REQUEST)


class FakeCardGameAPIList(generics.ListAPIView):
    queryset = FakeCardGame.objects.all()
    serializer_class = FakeCardGameSerializer

    def get_queryset(self):
        index = [i for i in range(1, FakeCardGame.objects.count() + 1)]
        random_index = random.sample(index, 5)
        return FakeCardGame.objects.filter(pk__in=random_index)
