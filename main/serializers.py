from .models import FakeNews, FakeCardGame
from rest_framework import serializers


class FakeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeNews
        fields = '__all__'


class FakeCardGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeCardGame
        fields = '__all__'
