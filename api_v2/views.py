import json

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from django.views import View
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer, ArticleModelsSerializer
from webapp.models import Article


# Create your views here.


class ArticleView(APIView):
    serializer_class = ArticleModelsSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        articles_data = self.serializer_class(articles, many=True).data
        return Response(articles_data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ArticleCrudView(APIView):

    def get(self, request, article_pk, *args, **kwargs):
        article_instance = self.get_object(article_pk)
        if not article_instance:
            return Response(
                {"res": "Статьи с таким pk не существует"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, article_pk, *args, **kwargs):
        article_instance = self.get_object(article_pk)
        if not article_instance:
            return Response(
                {"res": "Статьи с таким pk не существует"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
        }
        serializer = ArticleSerializer(instance=article_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_pk, *args, **kwargs):
        article_instance = self.get_object(article_pk)
        if not article_instance:
            return Response(
                {"res": "Статьи с таким pk не существует"},
                status=status.HTTP_400_BAD_REQUEST
            )
        article_instance.delete()
        return Response(
            {"res": "Статья удалена!"},
            status=status.HTTP_200_OK
        )
