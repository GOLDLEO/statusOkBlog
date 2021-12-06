from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# exceptions import


from .serializers import *

from .models import Post, Tag

from django.http import HttpResponse


@api_view(['GET'])
def list_of_posts(request):
    """ List of last posts """
    if request.method == 'GET':
        data = []
        posts = [post for post in Post.objects.all() if post.is_active is True]
        tags = Tag.objects.all()
        serializer = PostSerializer(posts, context={'request': request}, many=True)
        serializer_tags = TagSerializer(tags, context={'request': request}, many=True)
        return Response({
            'data': serializer.data,
            'tags': serializer_tags.data,
        })
    else:
        return Response('ne ok', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def posts_by_tag(request, *args):
    """  List of posts by tags or tag """
    if request.method == 'GET':
        arg_tags = request.GET.get('tags').split(',')
        posts = []
        print('args tags: ',  arg_tags)
        for tag in arg_tags:
            tag = tag.title()
            try:
                t = Tag.objects.get(name=tag)
            except Tag.DoesNotExist as err:
                print(err)
                return Response('Попробуйте применить другой тег. ', status=status.HTTP_404_NOT_FOUND)
            print('>> tag: ', t)
            list_post_by_tag = [post for post in Post.objects.filter(tag_name=Tag.objects.get(name=str(tag))) if post.is_active is True]
            print(list_post_by_tag)
        serializer_posts = PostSerializer(list_post_by_tag,context={'request': request}, many=True)
        return Response({
            'data': serializer_posts.data,
        })


@api_view(['GET'])
def post_detail(request, pk):
    if request.method == 'GET':
        try:
            post = Post.objects.filter(pk=pk)

            # update count views
            post_for_add = Post.objects.filter(pk=pk).update(count_view=post[0].count_view+1)
        except IndexError:
            return Response({
                "status_code": 404,
                'error_message': 'Статья не найдена.',
            }, status=status.HTTP_404_NOT_FOUND)

        serializer_post = PostSerializer(post, context={'request': request}, many=True)
        return Response({
            'data': serializer_post.data
        })

    else:
        return Response({
            'status_code': 405,
            "error_message": 'Now allowed methods. We are sorry..',
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)