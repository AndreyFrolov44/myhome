from django.db import models
from phone_field import PhoneField


POSITION = (
    ('about', 'about',),
    ('contact', 'contact',),
)


class Service(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    svg = models.FileField(upload_to='about')

    def __str__(self):
        return self.title


class Feature(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=30)
    svg = models.FileField(upload_to='about')

    def __str__(self):
        return self.title


class Realtor(models.Model):
    name = models.CharField(max_length=60)
    specialty = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    pinterest = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    image = models.ImageField(upload_to='about', blank=True, null=True)

    def __str__(self):
        return self.name


class Static(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()
    position = models.CharField(max_length=20, choices=POSITION, unique=True)

    def __str__(self):
        return self.position
