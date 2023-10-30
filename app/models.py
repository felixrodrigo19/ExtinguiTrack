from django.db import models


class Manufacture(models.Model):
    description = models.CharField(max_length=150)
    website = models.CharField(max_length=300)


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    phone = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    website = models.CharField(max_length=300)


class Location(models.Model):
    description = models.CharField(max_length=150)
    building = models.CharField(max_length=150)
    floor = models.CharField(max_length=10)


class Agent(models.Model):
    description = models.CharField(max_length=50)


class Capacity(models.Model):
    capacity = models.DecimalField(max_digits=5, decimal_places=2)


class Type(models.Model):
    description = models.CharField(max_length=50)


class FireExtinguisher(models.Model):
    serial_number = models.CharField(max_length=20)
    manufacturing_date = models.DateField()
    last_inspection_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
