from django.db import models
from .validators import email_validator
# Create your models here.


class Address(models.Model):

    city = models.CharField(max_length=32)
    street_name = models.CharField(max_length=64)
    street_number = models.IntegerField()
    apartment_number = models.IntegerField(null=True)

    class Meta:

        unique_together = (("city", "street_name", "street_number", "apartment_number"),)


class Telephone(models.Model):

    number = models.IntegerField(unique=True)
    type = models.CharField(max_length=32)


class Person(models.Model):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    telephone = models.ForeignKey(Telephone, on_delete=models.CASCADE, null=True)


class Email(models.Model):

    email_address = models.CharField(max_length=64, unique=True, validators=[email_validator])
    type = models.CharField(max_length=32)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)


class Groups(models.Model):

    name = models.CharField(max_length=32, unique=True)
    member = models.ManyToManyField(Person)
