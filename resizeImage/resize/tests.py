from django.http import response
from django.test import TestCase
from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
#from django.urls.base import resolve
from resize.views import resize_picture
from .models import Image
import os
from pathlib import Path
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from PIL import Image as PIL_image
from django.db.models import ImageField



class TestUrls(SimpleTestCase):

    def test_image_url_is_resolved(self):
        url = reverse('image')
        self.assertEquals(resolve(url).func.view_class,resize_picture)

class test_image(ImageField):
    def __init__(self,path):
        self.path = path
        self.image = PIL_image.open(path)
        
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.image_url = reverse('image')
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR, 'media'),'pictures')
        self.image_path = os.path.join( self.MEDIA_ROOT,'default.jpg')


    def test_resize_picture_get(self):
        response = self.client.get(self.image_url)
        self.assertEquals(response.status_code, 200)


    def test_resize_picture_post(self):
        response = self.client.post(self.image_url,{
            #'image': PIL_image.open(self.image_path),
            'width' : 100,
            'height' : 114,

        })
        self.assertEqual(response.status_code, 201)


    