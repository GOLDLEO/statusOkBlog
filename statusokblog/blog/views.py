from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *

from .models import Post


@api_view(['GET'])
def list_of_posts(request):
    """ List of last posts """
    if request.method == 'GET':
        data = []
        posts = Post.objects.all()
        data = posts
        serializer = PostSerializer(data, context={'request': request}, many=True)
        return Response({
            'data': serializer.data,
        })
    else:
        return Response('ne ok', status=status.HTTP_400_BAD_REQUEST)