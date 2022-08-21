from django.urls import path
from .views import all_posts,post_details


urlpatterns=[
path('',all_posts),
path('<int:id>',post_details),


]