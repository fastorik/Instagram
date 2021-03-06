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
        fields = ['id','image' ,'video', 'postContent', 'author', 'likes', 'saveSystem']
        read_only_fields = ['author']
        permission_classes = (IsAuthenticatedOrReadOnly)

    def validate(self, data):
        for user in data['likes']:
            currentUser = self.context['user']
            if user.id != currentUser.id:
                raise serializers.ValidationError(
                'Not a user')
            for user in data['saveSystem']:
                if user.id != currentUser.id:
                    raise serializers.ValidationError(
                    'Not a user')
        return data

    def create(self, validated_data):
        author_id = self.context['post_author_id']
        return Post.objects.create(author_id=author_id, **validated_data)


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaggedItem
#         fields = ['tag']

class PostSerializerView(serializers.ModelSerializer):
    allComments = SimpleCommentSerializer(
        many=True, required=False, read_only=True)
    author = UserSerializerExpanded()
    class Meta:
        model = Post
        fields = ['id' ,'image', 'video', 'postContent', 'author','total_likes', 'likes','allComments']

class LikeSerializer(serializers.ModelSerializer):
    # likes1 = serializers.SerializerMethodField(method_name='likes')
    # def likes(self, post:Post):
    #     user = self.context['post_author_id']
    #     pk  = self.context['pk']
    #     like = post.likes.through.objects.get(post_id=pk['pk'], newuser_id=user)
    #     user_id = like.newuser_id
    #     print(user_id)
    #     return user_id

    def validate(self, data):
        for user in data['likes']:
            currentUser = self.context['user']
            if user.id != currentUser.id:
                raise serializers.ValidationError(
                'Not a user')
            for user in data['saveSystem']:
                if user.id != currentUser.id:
                    raise serializers.ValidationError(
                    'Not a user')
        return data

    class Meta:
        model = Post
        fields = ['likes', 'saveSystem']


# class TagUnrelatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaggedItem
#         fields = ['tag']

# class PostSerializerTags(PostSerializer):
#     tags = TagUnrelatedSerializer()

#     class Meta(PostSerializer.Meta):
#         fields = (*PostSerializer.Meta.fields, 'tags')

# class TagSerializer(TagUnrelatedSerializer):
#     post = PostUnrelatedSerializer(many = True)
#     class Meta(TagUnrelatedSerializer.Meta):
#         fields = (*TagUnrelatedSerializer.Meta.fields, 'tags')