from django.db import models
from django.contrib.auth.models import User
from PIL import Image as PIL_image
from rest_framework.authtoken.models import Token
import os
import hashlib
from resizeImage.settings import logger

class Image(models.Model):

    def path_and_rename(instance, filename):
        upload_to = 'pictures'
        image_path = instance.image.url
        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)
        w = instance.width
        h = instance.height if instance.height > 0 else w
        hash_name = hashlib.md5(name.encode())
        new_filename = str(hash_name) + f'_{w}x{h}{ext}'
        return os.path.join(upload_to, new_filename)        


    image = models.ImageField(default='default.jpg', upload_to=path_and_rename)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)

        img = PIL_image.open(self.image.path)
        w = self.width
        h = self.height if self.height>0 else w
        output_size = (w, h)
        img.thumbnail(output_size)
        img.save(self.image.path)

