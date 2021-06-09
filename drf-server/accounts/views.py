from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import jwt

from decouple import config

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    
    # 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 팔로우
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    target_person = get_object_or_404(get_user_model(), pk=user_pk)
    request_person = request.user

    if target_person != request_person:
        if target_person.followers.filter(pk=request_person.pk).exists():
            target_person.followers.remove(request_person)
            followed = False
        else:
            target_person.followers.add(request_person)
            followed = True
    follow_status = {
        'followed' : followed,
        'followersCount' : target_person.followers.count(),
        'followingsCount' : target_person.followings.count(),
    }
    return JsonResponse(follow_status)


@api_view(['POST'])
def verify_user(request):
    SECRET_KEY = config("SECRET_KEY")
    decoded = jwt.decode(request.data.get('token'), SECRET_KEY, algorithms=["HS256"])
    user_id = decoded.get('user_id')
    username = decoded.get('username')
    you = get_object_or_404(get_user_model(), pk=user_id)
    superuser_status = True if you.is_superuser else False
    user_info = {
        'username': username,
        'user_id': user_id,
        'issuperuser': superuser_status,
    }
    return JsonResponse(user_info)


def userinfo(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    username = user.username
    user_info = {
        'username' : username,
    }
    return JsonResponse(user_info)


def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    like_articles = user.like_articles.all()
    like_articles_json = []
    for like_article in like_articles:
        like_articles_json.append(
            {  
                'id' : like_article.id,
                'user_id' : like_article.user_id,
                'title' : like_article.title,
                'categories' : like_article.categories,
                'content' : like_article.content,
                'created_at' : like_article.created_at,
                'updated_at' : like_article.updated_at,
            }
        )

    like_movies = user.like_movies.all()
    like_movies_json = []
    for like_movie in like_movies:
        like_movies_json.append(
            {  
                'id' : like_movie.id,
                'title' : like_movie.title,
                'poster_path' : like_movie.poster_path,
            }
        )

    like_reviews = user.like_reviews.all()
    like_reviews_json = []
    for like_review in like_reviews:
        like_reviews_json.append(
            {
                'id' : like_review.id,
                'movie' : like_review.movie.title,
                'movie_id' : like_review.movie.id,
                'title' : like_review.title,
                'content' : like_review.content,
            }
        )

    create_articles = user.articles.all()
    create_articles_json = []
    for create_article in create_articles:
        create_articles_json.append(
            {
                'id' : create_article.id,
                'user_id' : create_article.user_id,
                'title' : create_article.title,
                'categories' : create_article.categories,
                'content' : create_article.content,
                'created_at' : create_article.created_at,
                'updated_at' : create_article.updated_at,
            }
        )

    create_reviews = user.reviews.all()
    create_reviews_json = []
    for create_review in create_reviews:
        create_reviews_json.append(
            {
                'id' : create_review.id,
                'movie' : create_review.movie.title,
                'movie_id' : create_review.movie.id,
                'rank': create_review.rank,
                'title' : create_review.title,
                'content' : create_review.content,
            }
        )

    followers = user.followers.all()
    followers_json = []
    for follower in followers:
        followers_json.append(follower.id)

    followings = user.followings.all()
    followings_json = []
    for following in followings:
        followings_json.append(following.id)

    likemovies = user.like_movies.all()
    cnt_genres = []
    for likemovie in likemovies:
        genres = likemovie.genres.all()
        for genre in genres:
            cnt_genres.append(genre.name)

    from collections import Counter
    cnt_result = Counter(cnt_genres)
    favorite_genre = cnt_result.most_common()[0][0] if cnt_result else '없음'

    # create_votes = user.votes.all()
    user_info = {
        'username': user.username,
        'user_id': user.id,
        'like_articles' : like_articles_json,
        'like_movies' : like_movies_json,
        'like_reviews' : like_reviews_json,
        'create_articles': create_articles_json,
        'create_reviews': create_reviews_json,
        'followers': followers_json,
        'followings': followings_json,
        'favorite_genre': favorite_genre,
    }
    return JsonResponse(user_info)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteaccount(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    if user.id == request.user.id:
        user.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)