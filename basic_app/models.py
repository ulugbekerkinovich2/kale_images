from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Image(models.Model):
    code = models.CharField(max_length=50, unique=False)
    image = models.ImageField(upload_to='images/')
    compressed_image = ImageSpecField(source='image',
                                      processors=[ResizeToFill(800, 800)],
                                      format='PNG',
                                      options={'quality': 60})

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
