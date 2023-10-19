from django.db import models


# Create your models here.
class Image(models.Model):
    code = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
