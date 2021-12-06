from django.urls import path
from .views import list_of_posts, posts_by_tag, post_detail

urlpatterns = [
    path('api/posts/', list_of_posts),
    path('api/posts/tags/', posts_by_tag),  # localhost:8000/blog/api/posts/tags/?tags=Python
    path('api/post/<int:pk>', post_detail),
]
