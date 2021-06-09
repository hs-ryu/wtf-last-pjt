from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# 게시글 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def createarticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 모든 게시글 조회
@api_view(['GET'])
def getallarticles(request):
    articles = Article.objects.order_by('-pk')
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

# 게시글 좋아요
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def likearticle(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        liked = False
    else:
        article.like_users.add(request.user)
        liked = True
    like_status = {
        'liked' : liked,
        'likeCount' : article.like_users.count(),
    }
    return JsonResponse(like_status)

# 게시글 상세 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def getarticle(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

# 게시글 수정
@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def updatearticle(request, article_pk):
    if not request.user.articles.filter(pk=article_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
# 게시글 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def deletearticle(request, article_pk):
    if not request.user.articles.filter(pk=article_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response({'id' : article_pk})

# 게시글의 댓글 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def createcomment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    #여기서 막히네. 해결!
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user) # 이 시점에 어떤 게시글에 달린 댓글인지에 대한 정보를 추가해줘야함.
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 게시글의 댓글들 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def getallcomments(request, article_pk):
    comments = Comment.objects.filter(article_id=article_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 게시글의 댓글 수정
@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def updatecomment(request, article_pk, comment_pk):
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 게시글의 댓글 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def deletecomment(request, article_pk, comment_pk):
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response({'id' : comment_pk})