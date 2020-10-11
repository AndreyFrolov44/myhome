from django.urls import path
from .views import HomeListView, load_more, HomeDetailView, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('listings/', HomeListView.as_view(), name='listings'),
    path('listings/lazy_load_posts/', load_more, name='load_more'),
    path('listings/<slug:slug>/', HomeDetailView.as_view(), name='listing_detail'),
]
