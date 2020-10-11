from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Home


class Index(View):
    def get(self, request):
        slider_objects = Home.objects.filter(slider=True)
        featured_properties = Home.objects.filter(featured_properties=True)
        hot_deal = Home.objects.get(hot_deal=True)
        return render(request, 'home/index.html', context={'slider_objects': slider_objects,
                                                           'featured_properties': featured_properties,
                                                           'hot_deal': hot_deal})


def load_more(request):
    offset = int(request.POST['offset'])
    limit = 3
    posts = Home.objects.all()[offset:limit+offset]
    totalData = Home.objects.count()
    data = {}
    posts_json = serializers.serialize('json', posts)
    return JsonResponse(data={
        'posts': posts_json,
        'totalResult': totalData,
    })


class HomeListView(ListView):
    template_name = 'listing/listings.html'
    model = Home
    paginate_by = 3


class HomeDetailView(DetailView):
    template_name = 'listing/listingDetail.html'
    model = Home
