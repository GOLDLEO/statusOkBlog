from django.urls import path
from .views import list_of_posts

urlpatterns = [
    path('api/posts/', list_of_posts),

]
