from django.db import models
from django.contrib.auth.models import User

# Create your models here.

RATE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),

]

class School(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField(blank=True, null=True)
    rating_location = models.IntegerField(blank=True, null=True)
    rating_opportunities = models.IntegerField(blank=True, null=True)
    rating_facilities = models.IntegerField(blank=True, null=True)
    rating_food = models.IntegerField(blank=True, null=True)
    rating_clubs = models.IntegerField(blank=True, null=True)
    rating_social = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    body = models.TextField()
    location = models.IntegerField(choices=RATE_CHOICES)
    opportunities = models.IntegerField(choices=RATE_CHOICES)
    facilities = models.IntegerField(choices=RATE_CHOICES)
    food = models.IntegerField(choices=RATE_CHOICES)
    clubs = models.IntegerField(choices=RATE_CHOICES)
    social = models.IntegerField(choices=RATE_CHOICES)

    overall = models.IntegerField(blank=True, null=True)



    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class FakeShool(models.Model):
    address = models.TextField()

    def __str__(self):
        return self.address
