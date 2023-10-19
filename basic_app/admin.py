from django.contrib import admin

from basic_app.models import Image

# Register your models here.
admin.site.site_header = 'Администрирование сайта'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'Администрирование сайта'
admin.site.register(Image)
