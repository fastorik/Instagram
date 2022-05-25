from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer, PostSerializerNoLikes, PostSerializerView, LikeSerializer
from rest_framework.response import Response
from rest_framework import status

class PostViewSet(ModelViewSet):

    def get_queryset(self):
        return Post.objects.select_related('author').\
        prefetch_related('allComments__author').\
        prefetch_related('likes').\
        prefetch_related('saveSystem').\
        prefetch_related('tags')


    def get_serializer_context(self):
        return {'post_author_id': self.request.user.id, 
                'user':self.request.user,
                'pk': self.request.parser_context.get('kwargs'),
                'request': self.request
                }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializerView
        elif self.request.method == 'PUT': 
            pk  = self.request.parser_context.get('kwargs')
            post = Post.objects.get(id = pk['pk'])
            if self.request.user.id != post.author_id: 
                return LikeSerializer 
            else: 
                return PostSerializer
        elif self.request.method == 'DELETE':
            return Response(status=status.HTTP_204_NO_CONTENT)
        return PostSerializerNoLikes

    # def perform_create(self, serializer):
    #     serializer.save()
    # def update(self, request, *args, **kwargs):
    #     pers = request.user.id
    #     post = Post.objects.get(id = kwargs['pk'])
    #     if pers == post.author.id:
    #         partial = kwargs.pop('partial', True)
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)
    #     elif pers != post.author.id:
    #         # serializer = LikeSerializer(data=request.data)
    #         # serializer.is_valid(raise_exception=True)
    #         # serializer.save()
    #         # return Response(serializer.data)
    #         return Response({'error': 'Not an author'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
