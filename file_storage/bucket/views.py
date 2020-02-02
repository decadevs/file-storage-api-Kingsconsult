from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bucket
from . import models
from .serializers import BucketSerializer
from . import serializers

