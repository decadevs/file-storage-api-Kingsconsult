from django.test import TestCase
from .models import Bucket
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from . import views


# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.bucket_name = "Create the bucket name"
        self.bucket = Bucket(name=self.bucket_name)
        
    def test_to_create_bucket(self):
        old_bucket_count = Bucket.objects.count()
        self.bucket.save()
        new_bucket_count = Bucket.objects.count()
        self.assertNotEqual(old_bucket_count, new_bucket_count)
        
class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.bucket_data = {'name': 'Django docs'}
        self.response = self.client.post(views.CreateBucket(), self.bucket_data, format="json")

    def test_api_can_create_a_bucket(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_get_a_bucket(self):
        """Test the api can get a given bucket."""
        bucket = Bucket.objects.all()
        response = self.client.get(reverse('detail',
            kwargs={'pk': bucket[0]['id']}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucket)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucket."""
        bucket = Bucket.objects.get()
        change_bucket = {'name': 'Something new'}
        res = self.client.put(
            reverse('update', kwargs={'pk': bucket.id}),
            change_bucket, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucket = Bucket.objects.get()
        response = self.client.delete(
            reverse('delete', kwargs={'pk': bucket.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)