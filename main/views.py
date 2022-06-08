from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
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
        news = FakeNews.objects.create(description=request.data['description'],
                                       answer=answer,
                                       correct=correct)

        return Response({'news': model_to_dict(news)})


class FakeCardGameAPIList(generics.ListAPIView):
    queryset = FakeCardGame.objects.all()
    serializer_class = FakeCardGameSerializer

    def get_queryset(self):
        index = [i for i in range(1, FakeCardGame.objects.count() + 1)]
        random_index = random.sample(index, 5)
        return FakeCardGame.objects.filter(pk__in=random_index)
