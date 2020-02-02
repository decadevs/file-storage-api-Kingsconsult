# Generic view
from django.urls import path

from . import views

app_name = 'buckets'
urlpatterns = [
    path('', views.BucketList.as_view()),

]

# # Normal view (hard way to write view)
# from . import views
# from django.urls import path

# app_name = 'buckets'
# urlpatterns = [
#     path('', views.bucket, name='index'),
#     path('<int:bucket_id>/', views.detail, name='detail'),

# ]
