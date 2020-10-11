from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Contact
from about.models import Static


class ContactView(View):
    def get(self, request):
        static_text = get_object_or_404(Static, position='contact')
        address = Contact.objects.get(type='address')
        phone = Contact.objects.get(type='phone')
        email = Contact.objects.get(type='email')
        return render(request, 'contact/contact.html', context={
            'static_text': static_text,
            'address': address,
            'phone': phone,
            'email': email
        })
