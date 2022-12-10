from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import AnimalSerializer, BagSerializer
from .models import Animal, Bag
from rest_framework.views import APIView

# Create your views here.


class AnimalView(APIView):

    def get(self, request):
        animals = Animal.objects.all()
        return Response(AnimalSerializer(animals, many=True).data)

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BagView(APIView):

    def get(self, request):
        bags = Bag.objects.all()
        return Response(BagSerializer(bags, many=True).data)

    def post(self, request):
        serializer = BagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = BagSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     bag = Bag(
    #         length=request.data.get('length'),
    #         height=request.data.get('height'),
    #         width=request.data.get('width'),
    #         color=request.data.get('color'),
    #     )
    #     bag.volume = bag.length * bag.height * bag.width
    #     bag.save()
    #     return Response(BagSerializer(bag).data)

