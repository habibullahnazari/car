from .models import *


def footer_context(request):
    footer_info = About_footer.objects.first()
    return {'footer_info': footer_info}


def address_context(request):
    address_info = Address.objects.first()
    return {'address_info': address_info}


def social_context(request):
    social_media = SocialMedia.objects.first()
    return {'social_media': social_media}


def openinghour_context(request):
    openhour = OpeningHours.objects.filter(status='ON')
    offhour = OpeningHours.objects.filter(status='OFF')
    return {'on': openhour, 'off': offhour}


def all_head_des(request):
    message = All_HeadDes.objects.first()
    return {"allmessage": message}


def about_context(request):
    about = About.objects.first()
    return {'about': about}


def services(request):
    all_services = Service.objects.all()
    return {'service': all_services}


def allmeta(request):
    all_metas = AllMeta.objects.first()
    return {'all_meta': all_metas}
