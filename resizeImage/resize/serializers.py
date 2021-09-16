from rest_framework import serializers
from .models import Image
from PIL import Image as PIL_image
import os
from django.core.files.storage import FileSystemStorage
from resizeImage.settings import BASE_DIR
from resizeImage.settings import logger


class ImageSerializer(serializers.ModelSerializer):
    #image_url = serializers.SerializerMethodField('get_image_url')
    #image = serializers.ImageField(default='default.jpg')
    #width = serializers.IntegerField()
    #height = serializers.IntegerField()
    MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR, 'media'),'pictures')
    #print (f'BASE_DIR:{BASE_DIR}')

    class Meta:
        model = Image
        fields = ('image','width','height')


    def get_image_url(self, obj):
        return obj.path
 
    def validate(self, data):
        image_name = data['image'].name if 'image' in data.keys() else  'default.jpg'
        image_name, ext = os.path.splitext(image_name)
        image_width = data['width']
        image_height = data['height'] if 'height' in data.keys() else image_width

        new_filename = image_name + f'_{image_width}x{image_height}{ext}'
        image_path = os.path.join( self.MEDIA_ROOT,new_filename)
        print(f'image_path: {image_path}')
        if os.path.exists(image_path):
            logger.info(f'The image {new_filename} already exits. The image won\'t be added.')
            raise serializers.ValidationError("The image already exits. The image won't be added.'")
        else:
            logger.info(f'The image {new_filename} has added.')
            return data