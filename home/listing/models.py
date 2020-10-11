from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


TYPE_CHOICE = (
    ('Home', 'Home'),
    ('Garage', 'Garage'),
    ('Flat', 'Flat'),
)

RENT_OR_SALE = (
    ('For rent', 'For rent'),
    ('For sale', 'For sale'),
)


class Home(models.Model):
    title = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    type = models.CharField(max_length=40, choices=TYPE_CHOICE)
    rent_or_sale = models.CharField(max_length=10, choices=RENT_OR_SALE)
    sq_ft = models.IntegerField()
    baths = models.IntegerField(blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    garages = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    features = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='home')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=50)
    featured_properties = models.BooleanField(default=False)
    hot_deal = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    available = models.BooleanField(default=True)

    def get_list(self):
        if self.features:
            return self.features.split(',')
        else:
            return

    def get_absolute_url(self):
        return reverse('listing_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


