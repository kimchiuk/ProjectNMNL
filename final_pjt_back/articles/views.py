from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Article, Comment
from .serializers import *


# Create your views here.
# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# @permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
@authentication_classes([TokenAuthentication])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        data = serializer.data
        data['liked'] = article.likes.contains(request.user)
        return Response(data)
    
    #  수정 삭제
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    # 게시글 좋아요
    elif request.method == 'POST':
        user = request.user
        if user in article.likes.all():
            article.likes.remove(user)
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            article.likes.add(user)
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)
        
        
        

# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def comment_list(request, article_pk):

    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        comments = get_list_or_404(Comment, article=article_pk)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.user)
            serializer.save(article=article, user=request.user)
            return Response(serializer.data)
        

# @permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
