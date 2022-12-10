from django.urls import path
from .views import *

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('bags/', BagView.as_view()),
    # path('animal/<int:pk>/', AnimalDetailView.as_view()),
    # path('animal/add/bag/', AnimalAddBagView.as_view()),
    # # path('animals/', AnimalListView.as_view()),
    # # path('animal/<int:pk>/', AnimalDetailView.as_view()),
]
