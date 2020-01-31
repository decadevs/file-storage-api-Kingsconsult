from django.test import TestCase
import datetime

# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.bucket_name = "Create the bucket name"
        self.bucket = bucket(name=self.bucket_name)
        
    def test_to_create_bucket(self):
        old_bucket_count = bucket.objects.count()
        self.bucket.save()
        new_bucket_count = bucket.objects.count()
        self.assertNotEqual(old_bucket_count, new_bucket_count)