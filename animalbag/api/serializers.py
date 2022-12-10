from rest_framework import serializers
from .models import *


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"

    def create(self, validated_data):
        animal = Animal(
            name=validated_data.get('name'),
            age=validated_data.get('age'),
            weight=validated_data.get('weight'),
            color=validated_data.get('color'),
        )
        animal.save()
        return animal


class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = "__all__"

    def create(self, validated_data):
        bag = Bag(
            length=validated_data.get('length'),
            height=validated_data.get('height'),
            width=validated_data.get('width'),
            color=validated_data.get('color'),
        )
        bag.volume = bag.length * bag.height * bag.width
        bag.save()
        return bag

