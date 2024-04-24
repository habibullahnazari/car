from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.


def home(request):
    slider = Slider.objects.all()
    gall_photo = Gallery.objects.all()
    return render(request, 'Car/index.html', {'photos': gall_photo, 'slider': slider})


def contactus(request):
    if request.method == "POST":
        contactus = Contactus()
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("tel")
        address = request.POST.get("address")
        message = request.POST.get("message")

        contactus.name = name
        contactus.email = email
        contactus.phone = phone
        contactus.address = address
        contactus.message = message
        # contactus.recieve_date = date1
        try:
            contactus.save()
            messages.success(request, "Data inserted successfully")
        except:
            messages.warning(request, "Data was not inserted")
    return render(request, 'Car/contact.html')


def quotev(request):
    if request.method == 'POST':
        quote = Quote()
        make = request.POST.get("make")
        model = request.POST.get("model")
        year = request.POST.get("year")
        suburb = request.POST.get("suburb")
        name = request.POST.get("name")
        phone = request.POST.get("tel")
        email = request.POST.get("email")
        message = request.POST.get("message")
        quote.make = make
        quote.model = model
        quote.year = year
        quote.suburb = suburb
        quote.name = name
        quote.phone = phone
        quote.email = email
        quote.message = message
        quote.save()
        return HttpResponse("<h1> your submission was successful </h1>,<br> <h1> <a href='qt'>Back</a></h1>")
    return render(request, 'Car/getquote.html')


def blog(request):
    all_post = Post.objects.filter(status='published')
    all_post = all_post[0:9]

    return render(request, 'Car/blog.html', {'posts': all_post})


def galleryv(request):
    gallery = Gallery.objects.all()[0:30]
    return render(request, 'Car/gallery.html', {'gallery': gallery})


def spabout(request):
    return render(request, 'Car/about.html')


def service(request):
    return render(request, 'Car/service.html')


def stuff(request):
    all_stuff = Stuff.objects.all()
    return render(request, 'Car/stuff.html', {'stuffs': all_stuff})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'Car/blog-details.html', {'post': post})
