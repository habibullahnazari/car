from django.urls import path
from .views import *

app_name = 'Car'
urlpatterns = [
    path('', home, name="home"),
    path('contact', contactus, name="contact"),
    path('qt', quotev, name="qt"),
    path('blogs', blog, name="blog"),
    path('gallery', galleryv, name="gallery"),
    path('about', spabout, name='about'),
    path('services', service, name='service'),
    path('stuffs', stuff, name='stuff'),
    path('blog/<int:id>/', post_detail, name='post_detail')


]
