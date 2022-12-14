from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import AnimalListSerializer, CreateAnimalSerializer, \
                         CreateBagSerializer, BagListSerializer, BagDetailSerializer, \
                         AnimalDetailSerializer, UpdateAnimalSerializer, UpdateBagSerializer, \
                         DeleteBagSerializer, DeleteAnimalSerializer
from .models import Animal, Bag
from rest_framework.views import APIView

# Create your views here.


class AnimalListView(APIView):

    def get(self, request):
        animals = Animal.objects.all()
        return Response(AnimalListSerializer(animals, many=True).data)


class AnimalDetailView(APIView):

    def get(self, request, pk):
        try:
            animals = Animal.objects.get(pk=pk)
        except:
            return Response({"error": "Animal object does not exist."}, status=404)
        return Response(AnimalDetailSerializer(animals).data, status=200)


class AnimalCreateView(APIView):

    def post(self, request):
        serializer = CreateAnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AnimalUpdateView(APIView):

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed."}, status=404)
        try:
            instance = Animal.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists."}, status=404)

        serializer = UpdateAnimalSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

class BagUpdateView(APIView):

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed."}, status=404)
        try:
            instance = Bag.objects.get(pk=pk)
        except:
            return Response({"error": "Bag does not exists."}, status=404)

        serializer = UpdateBagSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)



class BagListView(APIView):

    def get(self, request):
        bags = Bag.objects.all()
        return Response(BagListSerializer(bags, many=True).data)


class BagDetailView(APIView):

    def get(self, request, pk):
        try:
            bag = Bag.objects.get(pk=pk)
        except:
            return Response({"error": "Bag object does not exist."}, status=404)
        return Response(BagDetailSerializer(bag).data)


class BagCreateView(APIView):

    def post(self, request):
        serializer = CreateBagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AddAnimalBagView(APIView):

    def post(self, request):
        animal = Animal.objects.filter(name=request.data.get('name'))
        bag = Bag.objects.filter(id=request.data.get('id'))
        if not animal:
            return Response({"error": "Animal object does not exist."}, status=404)
        elif not bag:
            return Response({"error": "Bag object does not exist."}, status=404)
        animal.bag_set.add(bag)
        animal.bags = animal.bag_set.count()
        animal.save()
        serializer = AnimalListSerializer(animal)
        return Response(serializer.data, status=201)


class DeleteBagView(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed."}, status=404)
        try:
            instance = Bag.objects.get(pk=pk)
        except:
            return Response({"error": "Bag does not exists."}, status=404)

        serializer = DeleteBagSerializer().delete(instance=instance)
        return Response({'message': 'Bag object was successfully deleted.'}, status=200)


class DeleteAnimalView(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed."}, status=404)
        try:
            instance = Animal.objects.get(pk=pk)
        except:
            return Response({"error": "Animal does not exists."}, status=404)

        serializer = DeleteAnimalSerializer().delete(instance=instance)
        return Response({'message': f'Animal object was successfully deleted.'}, status=200)
