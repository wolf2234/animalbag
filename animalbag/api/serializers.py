from rest_framework import serializers
from .models import *
from rest_framework.response import Response


# class RecursiveSerializer(serializers.Serializer):
#
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         return serializer.data


class AnimalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = "__all__"


class AnimalDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = "__all__"


class CreateAnimalSerializer(serializers.ModelSerializer):
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


class UpdateAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.weight = validated_data.get("weight", instance.weight)
        instance.color = validated_data.get("color", instance.color)
        # instance.bags = validated_data.get("bags", instance.bags)
        instance.save()
        return instance


class BagListSerializer(serializers.ModelSerializer):
    owner = AnimalListSerializer()

    class Meta:
        model = Bag
        fields = "__all__"


class BagDetailSerializer(serializers.ModelSerializer):
    owner = AnimalListSerializer()

    class Meta:
        model = Bag
        fields = "__all__"


class CreateBagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bag
        fields = "__all__"
        # fields = ("length", "height", "width", "color")

    def create(self, validated_data):
        bag = Bag(
            length=validated_data.get('length'),
            height=validated_data.get('height'),
            width=validated_data.get('width'),
            color=validated_data.get('color'),
        )
        animal = validated_data.get('owner', None)
        if animal:
            bag.owner = animal
            bag.volume = bag.length * bag.height * bag.width
            bag.save()
            animal.bags = animal.bag_set.count()
            animal.save()
        else:
            bag.volume = bag.length * bag.height * bag.width
            bag.save()
        return bag


class UpdateBagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bag
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.length = validated_data.get("length", instance.length)
        instance.height = validated_data.get("height", instance.height)
        instance.width = validated_data.get("width", instance.width)
        instance.color = validated_data.get("color", instance.color)
        instance.volume = instance.length * instance.height * instance.width
        if validated_data.get("owner") is None:
            if instance.owner is not None:
                instance.owner.bags = instance.owner.bags - 1
                instance.owner.save()
                instance.owner = None
            else:
                instance.owner = None
        else:
            instance.owner = validated_data.get("owner", instance.owner)
        instance.save()
        return instance


class DeleteBagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bag
        fields = "__all__"

    def delete(self, instance):
        instance.owner.bags = instance.owner.bags - 1
        instance.owner.save()
        return instance.delete()


class DeleteAnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = "__all__"

    def delete(self, instance):
        return instance.delete()
