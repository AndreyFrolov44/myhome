from django.db import models


TYPE_CHOICES = (
    ('address', 'address'),
    ('phone', 'phone'),
    ('email', 'email'),
)


class Contact(models.Model):
    text = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, unique=True)
    svg = models.FileField(upload_to='contact')

    def __str__(self):
        return self.type
