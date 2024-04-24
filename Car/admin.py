from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(About_footer)
admin.site.register(Slider)
admin.site.register(Address)
admin.site.register(SocialMedia)
admin.site.register(Gallery)
admin.site.register(OpeningHours)
admin.site.register(All_HeadDes)
admin.site.register(Stuff)
admin.site.register(About)
admin.site.register(Servicetype)
admin.site.register(Service)


class ContactusAdmin(admin.ModelAdmin):
    readonly_fields = ('recieve_date',)


admin.site.register(Contactus, ContactusAdmin)


@admin.register(Quote)
class Quatead(admin.ModelAdmin):
    list_display = ('make', 'model', 'suburb',
                    're_date', 'name', 'phone', 'email')


class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('re_date',)


@admin.register(Post)
class Postad(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish',
                    'status', 'created_date', 'update_date')
    list_filter = ('status', 'author', 'publish')
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    list_editable = ('status',)
    list_display_links = ('title', 'author', 'publish',
                          'created_date', 'update_date')
