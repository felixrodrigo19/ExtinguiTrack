from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Manufacture(models.Model):
    description = models.CharField(max_length=150)
    website = models.CharField(max_length=300)

    def __str__(self):
        return self.description


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    phone = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    website = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Location(models.Model):
    description = models.CharField(max_length=150)
    building = models.CharField(max_length=150)
    floor = models.CharField(max_length=10)

    def __str__(self):
        return self.description


class Agent(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Capacity(models.Model):
    capacity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.capacity)


class Type(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class FireExtinguisher(models.Model):
    serial_number = models.CharField(max_length=20)
    manufacturing_date = models.DateField()
    last_inspection_date = models.DateField()
    next_inspection_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)

    def __str__(self):
        return self.serial_number
