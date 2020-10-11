from django.contrib import admin
from .models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'rent_or_sale', 'price', 'author', 'date', 'featured_properties', 'hot_deal', 'slider', 'available',)
    list_editable = ('type', 'rent_or_sale', 'price', 'featured_properties', 'hot_deal', 'slider', 'available',)
    fields = (
        'title',
        'price',
        'address',
        ('type', 'rent_or_sale',),
        ('sq_ft', 'baths', 'beds', 'garages',),
        'description',
        'features',
        'image',
        'author',
        'slug',
        ('featured_properties', 'hot_deal', 'slider', 'available',)
    )
    prepopulated_fields = {'slug': ('title',)}


