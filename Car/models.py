from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='media/slider', height_field=None, width_field=None)
    message = models.CharField(max_length=200, default='')
    alt = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Address(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location


class About_footer(models.Model):
    name = models.CharField(max_length=200)
    desciption = models.TextField(
        max_length=280, help_text='maximum size is 280 character')
    logo = models.ImageField(upload_to='media/logo')
    pub_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    facebook = models.CharField(max_length=600, null=True, blank=True)
    x = models.CharField(max_length=600, null=True, blank=True)
    linkedin = models.CharField(max_length=600, null=True, blank=True)
    googleplus = models.CharField(max_length=600, null=True, blank=True)
    instagram = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return "all social media"


WEEKDAYS = [
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (7, _("Sunday")),


]

STATUS = [
    ('OFF', 'OFF'),
    ('ON', 'ON')
]


class OpeningHours(models.Model):

    weekday = models.IntegerField(null=True, blank=True, choices=WEEKDAYS)
    from_hour = models.TimeField(null=True, blank=True)
    to_hour = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=30, default='OFF', choices=STATUS)

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)

    def __str__(self):
        return self.get_weekday_display()


class Gallery(models.Model):
    photo_name = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to='media/Gallery', height_field=None, width_field=None, help_text='photo width =1200px height = 800')
    publish = models.DateTimeField(default=timezone.now)
    alt = models.CharField(max_length=30)

    def __str__(self):
        return self.photo_name

    class Meta:
        ordering = ('-publish',)


class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=250)
    message = models.CharField(max_length=900)
    recieve_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    suburb = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    re_date = models.DateField(auto_now_add=True)
    message = models.TextField(max_length=900)

    def __str__(self):
        return self.name + self.suburb


class All_HeadDes(models.Model):
    gallery_mes = models.CharField(max_length=170)
    slider_mes = models.CharField(max_length=170)
    service_mes = models.CharField(max_length=170)
    blog_mes = models.CharField(max_length=170)
    stuff_mes = models.CharField(max_length=170)


class Stuff(models.Model):
    name = models.CharField(max_length=50)
    photo = photo = models.ImageField(
        upload_to='media/stuff', height_field=None, width_field=None)
    job_position = models.CharField(max_length=100)
    facebook = models.URLField(max_length=200)
    x = models.URLField(max_length=200)
    gplus = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    photo = models.ImageField(
        upload_to='media/post', help_text='Image size should be width= 470x height=570')
    alt = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=40, default='ozzy auto recycle')
    aboutus = models.TextField(
        max_length=600, help_text='maximum character is 600')
    photo = models.ImageField(
        upload_to='media/about', help_text='Image size should be width= 800px height=650px')
    alt = models.CharField(max_length=20)
    slogan = models.TextField(
        max_length=150, help_text='max length is 150 character')

    def __str__(self):
        return self.title


class Servicetype(models.Model):
    services = models.CharField(max_length=50)

    def __str__(self):
        return self.services


class Service(models.Model):
    title = models.CharField(max_length=50)
    photo = photo = models.ImageField(
        upload_to='media/about', help_text='Image size should be width= 800px height=480px')
    description = models.TextField(max_length=700)
    service_type = models.ForeignKey(
        Servicetype, on_delete=models.CASCADE, related_name='service_type')
    alt = models.CharField(
        max_length=40, help_text='please meaning full name for photo', null=True, blank=True)

    def __str__(self):
        return self.title


class AllMeta(models.Model):
    about_meta_title = models.CharField(
        max_length=60, null=True, blank=True, help_text='meta title should be 50-60 character')
    about_meta_keyword = models.CharField(
        max_length=220, null=True, blank=True, help_text='meta keyword should be 10-20 meta keyword')
    about_meta_desc = models.CharField(max_length=160, null=True, blank=True,
                                       help_text='meta description should be 155-160 character')
    blog_meta_title = models.CharField(
        max_length=60, null=True, blank=True, help_text='meta title should be 50-60 character')
    blog_meta_keyword = models.CharField(
        max_length=220, null=True, blank=True, help_text='meta keyword should be 10-20 meta keyword')
    blog_meta_desc = models.CharField(
        max_length=160, null=True, blank=True, help_text='meta description should be 155-160 character')

    contact_meta_title = models.CharField(
        max_length=60, null=True, blank=True, help_text='meta title should be 50-60 character')
    contact_meta_keyword = models.CharField(
        max_length=220, null=True, blank=True, help_text='meta keyword should be 10-20 meta keyword')
    contact_meta_desc = models.CharField(
        max_length=160, null=True, blank=True, help_text='meta description should be 155-160 character')

    gallery_meta_title = models.CharField(
        max_length=60, null=True, blank=True, help_text='meta title should be 50-60 character')
    gallery_meta_keyword = models.CharField(
        max_length=220, null=True, blank=True, help_text='meta keyword should be 10-20 meta keyword')
    gallery_meta_desc = models.CharField(
        max_length=160, null=True, blank=True, help_text='meta description should be 155-160 character')

    quote_meta_title = models.CharField(
        max_length=60, null=True, blank=True, help_text='meta title should be 50-60 character')
    quote_meta_keyword = models.CharField(
        max_length=220, null=True, blank=True, help_text='meta keyword should be 10-20 meta keyword')
    quote_meta_desc = models.CharField(
        max_length=160, null=True, blank=True, help_text='meta description should be 155-160 character')

    index_meta_title = models.CharField(
        max_length=60, null=True, blank=True, help_text='meta title should be 50-60 character')
    index_meta_keyword = models.CharField(
        max_length=220, null=True, blank=True, help_text='meta keyword should be 10-20 meta keyword')
    index_meta_desc = models.CharField(
        max_length=160, null=True, blank=True, help_text='meta description should be 155-160 character')

    service_meta_title = models.CharField(
        max_length=60, null=True, blank=True, help_text='meta title should be 50-60 character')
    service_meta_keyword = models.CharField(
        max_length=220, null=True, blank=True, help_text='meta keyword should be 10-20 meta keyword')
    service_meta_desc = models.CharField(
        max_length=160, null=True, blank=True, help_text='meta description should be 155-160 character')

    def __str__(self):
        return "all_meta"
