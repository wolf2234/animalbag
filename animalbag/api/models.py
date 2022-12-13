from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    color = models.CharField(max_length=150)
    bags = models.IntegerField(default=0)

    def str(self):
        return f'{self.name} - {self.pk}'

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'


class Bag(models.Model):
    length = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    height = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    width = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    volume = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    color = models.CharField(max_length=150)
    owner = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)

    def str(self):
        return f'volume of bag = {self.volume}'

    class Meta:
        verbose_name = 'Bag'
        verbose_name_plural = 'Bags'

