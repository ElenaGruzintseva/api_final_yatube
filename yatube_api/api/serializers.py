from rest_framework.serializers import (CurrentUserDefault, ValidationError,
                                        ModelSerializer, SlugRelatedField)
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        default=CurrentUserDefault(),
        read_only=True,
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            ),
        )

    def validate_following(self, value):
        if self.context.get('request').user == value:
            raise ValidationError('Cannot follow oneself')
        return value


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
