from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import AnimalListSerializer, CreateAnimalSerializer, \
                         CreateBagSerializer, BagListSerializer
from .models import Animal, Bag
from rest_framework.views import APIView

# Create your views here.


class AnimalListView(APIView):

    def get(self, request):
        animals = Animal.objects.all()
        return Response(AnimalListSerializer(animals, many=True).data)


class AnimalCreateView(APIView):

    def post(self, request):
        serializer = CreateAnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BagListView(APIView):

    def get(self, request):
        bags = Bag.objects.all()
        return Response(BagListSerializer(bags, many=True).data)


class BagCreateView(APIView):

    def post(self, request):
        serializer = CreateBagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AddAnimalBagView(APIView):

    def post(self, request):
        animal = Animal.objects.get(name=request.data.get('name'))
        bag = Bag.objects.get(id=request.data.get('id'))
        animal.bag_set.add(bag)
        animal.bags = animal.bag_set.count()
        animal.save()
        serializer = AnimalListSerializer(animal)
        return Response(serializer.data, status=201)


