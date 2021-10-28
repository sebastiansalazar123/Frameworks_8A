from django.db import models
from django.db.models.base import Model

class country(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()

class city(models.Model) :
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()

class identification_type(models.Model) :
    type = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()

class user(models.Model) :
    first_name =models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    id_identification_type = models.ForeignKey(identification_type, on_delete=models.CASCADE)
    number_id = models.CharField(max_length=15)
    id_city = models.ForeignKey(city, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()

class session(models.Model) :
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    ip = models.CharField(max_length=200)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()

class race(models.Model) :
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()

class type (models.Model) :
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    abrev = models.CharField(max_length=4)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()

class pet(models.Model) :
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    status = models.BooleanField()
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_type = models.ForeignKey(type, on_delete=models.CASCADE)
    id_race = models.ForeignKey(race, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    delete_at = models.DateTimeField()







