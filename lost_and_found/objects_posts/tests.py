import os

from django.core.exceptions import ValidationError
from django.test import TestCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lost_and_found.settings')
import django
django.setup()

from lost_and_found.objects_posts.models import Post, Object


class PostModelTestCase(TestCase):
    def setUp(self):
        self.valid_object = Object.objects.create(
            name="Valid",
            image="https://img.modivo.cloud/product(f/f/2/f/ff2f579474e44e664d5dcb211bcae3f58073926b_03_0000303203719_MJ.jpg,jpg)/lacoste-antsug-wh1793-tmnosin-regular-fit-0000303203719.jpg",
            width=5,
            height=5,
            weight=5.5,
        )

    def test_profile_create_when_valid_object(self):
        p = Post(
            title='Valid String',
            description="Valid Description",
            author_name="Pesho",
            author_phone="0889696969",
            found=False,
            object=self.valid_object
        )
        p.full_clean()
        p.save()
        self.assertIsNotNone(p)

    def test_object_create_when_valid_all(self):
        o = self.valid_object
        o.full_clean()
        o.save()
        self.assertIsNotNone(o)

    def test_object_create_when_invalid_height(self):
        o = self.valid_object
        o.height = "aaa"
        with self.assertRaises(ValidationError):
            o.full_clean()
