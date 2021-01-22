from django.contrib import admin
from .models import *

class Timminginline(admin.StackedInline):
    model = Chamber.timming.through

class NearPlaceinline(admin.StackedInline):
    model = Chamber.nearest_places.through

class ChamberAdmin(admin.ModelAdmin):
    list_display =(
        'chamber_location',
        'region',
        'full_address',
        'phone1',
        'phone2',
    )
    inlines = [Timminginline,NearPlaceinline]

class AboutmeAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'whatsapp',
        'aboutme_english',
        'aboutme_hindi',
        'aboutme_bengali'
    )

class YoutubeAdmin(admin.ModelAdmin):
    list_display = (
        'link',
        'title',
        'description'
    )
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'img',
        'description',
    )

admin.site.register(Aboutme,AboutmeAdmin)
admin.site.register(Chamber, ChamberAdmin)
admin.site.register(Timming)
admin.site.register(NearPlace)
admin.site.register(Region)
admin.site.register(Announcement)
admin.site.register(Youtube,YoutubeAdmin)
admin.site.register(Gallery,GalleryAdmin)