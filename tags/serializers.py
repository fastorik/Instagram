# from posts.serializers import PostSerializer
# from posts.models import Post
# from rest_framework import serializers


# class TaggedObjectRelatedField(serializers.RelatedField):
#     def to_representation(self, value):
#         if isinstance(value, Post):
#             serializer = PostSerializer(value)
#         else:
#             raise Exception('Unexpected type of tagged object')
#         return serializer.data

