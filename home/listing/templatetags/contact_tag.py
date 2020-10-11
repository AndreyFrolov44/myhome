from django import template
from contact.models import Contact


register = template.Library()


@register.simple_tag()
def get_contacts():
    return {'address': Contact.objects.get(type='address'),
            'phone': Contact.objects.get(type='phone'),
            'email': Contact.objects.get(type='email')}
