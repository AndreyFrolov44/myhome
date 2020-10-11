from django.shortcuts import render
from django.views.generic.base import View

from .models import Static, Service, Realtor, Feature


class AboutView(View):
    def get(self, request):
        static_text = Static.objects.get(position='about')
        services = Service.objects.all()
        realtors = Realtor.objects.all()
        features = Feature.objects.all()
        return render(request, 'about/about.html', {'static_text': static_text,
                                                    'services': services,
                                                    'features': features,
                                                    'realtors': realtors})

