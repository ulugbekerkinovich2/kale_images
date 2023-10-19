from django.urls import path

from basic_app.views import return_image, post_images

urlpatterns = [
    path('image1/', return_image, name='return_image'),
    path('image1/post/', post_images, name='post_images')
]
