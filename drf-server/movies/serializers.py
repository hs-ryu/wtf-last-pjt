from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Comment, Movie, NowShowingMovie, Review, Vote, VoteComment

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'movie_id', 'poster_path', 'clicked', 'rank_average','release_date',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','movie_id', 'overview', 'poster_path', 'vote_average', 'netflix', 'watcha', 'wavve', 'naver', 'clicked','release_date', 'trailer', 'like_users', 'rank_average')
        read_only_fields = ('like_users',)


class NowShowingMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowShowingMovie
        fields = ('movieNm', 'openDt', 'audiAcc', 'image_path', 'userRating')

class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Review
        fields = ('id', 'title', 'rank','created_at', 'updated_at', 'username')

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Review
        fields = ('id', 'content','title', 'rank','created_at', 'updated_at', 'like_users', 'username')
        read_only_fields = ('like_users',)

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at', 'username')


class VoteListSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Vote
        fields = ('id','title', 'movie', 'option_one_count', 'option_two_count', 'option_one', 'option_two', 'username')

class VoteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Vote
        fields = ('id','title', 'option_one_count', 'option_two_count', 'username', 'created_at', 'updated_at', 'option_one', 'option_two')

class VoteCommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = VoteComment
        fields = ('id', 'choice', 'content', 'username', 'created_at', 'updated_at')