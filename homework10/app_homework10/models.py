from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=150)
    birthday = models.CharField(max_length=50)
    birth_place = models.CharField(max_length=150)
    bio = models.CharField(max_length=15000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    quote = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

