# from generic_relations.relations import GenericRelatedField
# from rest_framework import serializers
# from posts.models import Post
# from posts.serializers import PostSerializer
# from .models import TaggedItem
# class TagSerializer(serializers.ModelSerializer):
#     """
#     A `TaggedItem` serializer with a `GenericRelatedField` mapping all possible
#     models to their respective serializers.
#     """
#     content_object = GenericRelatedField({
#         Post: PostSerializer(),
#     })

#     class Meta:
#         model = TaggedItem
#         fields = ('tag', 'content_object')