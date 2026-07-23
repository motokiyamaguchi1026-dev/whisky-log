from django.db import models
from django.contrib.auth.models import User


class Whisky(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    distillery = models.CharField(max_length=100)

    country = models.CharField(max_length=50)

    age = models.IntegerField(
        null=True,
        blank=True
    )

    abv = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    memo = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):

    whisky = models.ForeignKey(
        Whisky,
        on_delete=models.CASCADE
    )

    drink_date = models.DateField()

    rating = models.IntegerField()

    memo = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.whisky.name} - {self.rating}"