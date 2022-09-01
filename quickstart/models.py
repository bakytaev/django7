from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

