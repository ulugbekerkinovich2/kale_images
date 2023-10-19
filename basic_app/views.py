import base64
import json
import os
from PIL import Image as PILImage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from basic_app.models import Image


# Create your views here.
def return_image(request):
    code = request.GET.get('code')
    if code is not None:
        image = get_object_or_404(Image, code=code)
        absolute_url = request.build_absolute_uri(image.image.url)
        return JsonResponse({'absolute_url': absolute_url})
    else:
        return JsonResponse({'error': 'Code parameter is missing'})


@csrf_exempt
def post_images(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code')
            image_data = request.FILES.get('image')
            if code is not None and image_data is not None:
                image = PILImage.open(image_data)
                image_name = f"{code}.png"
                image_path = os.path.join("images/", image_name)
                image.save(image_path, optimize=True, quality=6)
                Image.objects.create(code=code, image=image_path)
                return JsonResponse({'success': 'Image has been saved'})
            else:
                return JsonResponse({'error': 'Code or image is missing'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
