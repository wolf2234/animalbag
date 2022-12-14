# AnimalBag API

This is a simple test api that was written for educational purposes. It implements two objects, Animal and Bag, and the interaction between them.

## Frameworks:
- Django
- Django-rest-framework
- Python

## Databases:
- SQLite3

### List of endpoints:
```
- http://127.0.0.1:8000/api/v1/animals/ - get list animals.
- http://127.0.0.1:8000/api/v1/create/animal/ - create the animal object.
- http://127.0.0.1:8000/api/v1/animal/<int:pk>/ - get the animal object.
- http://127.0.0.1:8000/api/v1/update/animal/<int:pk>/ - update the animal object.
- http://127.0.0.1:8000/api/v1/delete/animal/<int:pk>/ - delete the animal object.
- http://127.0.0.1:8000/api/v1/add/animal/bag/ - add the bag object to the animal object.
- http://127.0.0.1:8000/api/v1/bags/ - get list bags.
- http://127.0.0.1:8000/api/v1/create/bag/ - create the bag object.
- http://127.0.0.1:8000/api/v1/bag/<int:pk>/ - get the object bag.
- http://127.0.0.1:8000/api/v1/update/bag/<int:pk>/ - update the object bag object.
- http://127.0.0.1:8000/api/v1/delete/bag/<int:pk>/ - delete the bag object.
```

### How to start:

```
cd animalbag
python manage.py runserver
```