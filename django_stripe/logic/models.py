from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Item(models.Model):
    currents = (('USD', 'USD'), ('EUR', 'EUR'))
    name = models.CharField(unique=True, max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.CharField(
        max_length=10,
        default='USD',
        choices=currents
    )

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=30, unique=True)
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    def __str__(self):
        return f'{self.name}({self.value}%)'


class Tax(models.Model):
    name = models.CharField(max_length=30, unique=True)
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return f'{self.name}({self.value}%)'


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)
    tax = models.ForeignKey(
        Tax,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    discount = models.ForeignKey(
        Discount,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.customer.email} order at {self.created_at}'
