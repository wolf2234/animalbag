from django.urls import path
from .views import *

urlpatterns = [
    path('animals/', AnimalListView.as_view()),
    path('create/animal/', AnimalCreateView.as_view()),
    path('create/bag/', BagCreateView.as_view()),
    path('bags/', BagListView.as_view()),
    path('add/animal/bag/', AddAnimalBagView.as_view()),
    # path('animal/<int:pk>/', AnimalDetailView.as_view()),
    # path('animal/add/bag/', AnimalAddBagView.as_view()),
    # # path('animals/', AnimalListView.as_view()),
    # # path('animal/<int:pk>/', AnimalDetailView.as_view()),
]
