from django.urls import path
from .views import list_of_posts, posts_by_tag

urlpatterns = [
    path('api/posts/', list_of_posts),
    path('api/posts/tags/', posts_by_tag),

]
