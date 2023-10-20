from django.contrib import admin

from basic_app.models import Image

# Register your models here.
admin.site.site_header = 'Администрирование сайта первый'
admin.site.site_title = 'Администрирование сайта первый'
admin.site.index_title = 'Администрирование сайта первый'


class ImageAdmin(admin.ModelAdmin):
    list_display = ('code', 'image')
    list_display_links = ('code', 'image')
    list_filter = ('code', 'image')
    search_fields = ('code', 'image')
    list_per_page = 25


admin.site.register(Image, ImageAdmin)
