# Relationships in Database Modeling (SQL)

# One to One
# Users Model
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.OneToOneField(Address, related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    street_address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

demon_dogs = Address.objects.create(
    street_address = "944 W. Fullerton Ave.",
    city = "Chicago",
    state = "IL",
    zip_code = "60614"
)

ciso = User.objects.create(
    first_name = "Narciso",
    last_name = "Lobo",
    address = demon_dogs
)

# One to Many
class Owner(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pet(models.Model):
    name = models.CharField(max_length=45)
    owner = models.ForeignKey(Owner, related_name='pets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

mr_smith = Owner.objects.create(
    name = 'Eric Smith'
)

bender = Pet.objects.create(
    name = "Bender",
    owner = mr_smith
)








# Many to Many

