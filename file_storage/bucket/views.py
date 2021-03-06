from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bucket
from . import models
from .serializers import BucketSerializer
from . import serializers

class BucketList(generics.ListAPIView):
    queryset = models.Bucket.objects.all()
    serializer_class = serializers.BucketSerializer
    
class CreateBucket(generics.ListCreateAPIView):
    queryset = models.Bucket.objects.all()
    serializer_class = serializers.BucketSerializer
    
class UpdateBucket(generics.RetrieveUpdateAPIView):
    queryset = models.Bucket.objects.all()
    serializer_class = serializers.BucketSerializer
    
class BucketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Bucket.objects.all()
    serializer_class = serializers.BucketSerializer
    
class DeleteBucket(generics.RetrieveDestroyAPIView):
    queryset = models.Bucket.objects.all()
    serializer_class = serializers.BucketSerializer
    
    
    
# class BucketView(APIView):
#     def get(self, request):
#         buckets = models.Bucket.objects.all()
#         return Response({"buckets": buckets})

