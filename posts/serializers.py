from rest_framework import serializers
from .models import Post
from comments.serializers import SimpleCommentSerializer
from user.models import NewUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserSerializerExpanded(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = [ 'user_name', 'name','avatar', 'gender']

class PostSerializerNoLikes(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','image' ,'video', 'postContent', 'author']
        read_only_fields = ['author']
        permission_classes = (IsAuthenticatedOrReadOnly)

    def create(self, validated_data):
        author_id = self.context['post_author_id']
        return Post.objects.create(author_id=author_id, **validated_data)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','image' ,'video', 'postContent', 'author', 'likes', 'save']
        read_only_fields = ['author']
        permission_classes = (IsAuthenticatedOrReadOnly)

    def create(self, validated_data):
        author_id = self.context['post_author_id']
        return Post.objects.create(author_id=author_id, **validated_data)


class PostSerializerView(serializers.ModelSerializer):
    allComments = SimpleCommentSerializer(
        many=True, required=False, read_only=True)
    author = UserSerializerExpanded()
    class Meta:
        model = Post
        fields = ['id' ,'image', 'video', 'postContent', 'author', 'total_likes', 'likes', 'allComments']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['likes', 'postContent']
        read_only_fields = ['postContent']

    # def create(self, validated_data):
    #     author_id = self.context['post_author_id']
    #     return Post.objects.create(author_id=author_id, **validated_data)
