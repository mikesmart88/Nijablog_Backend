from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from rest_framework.views import APIView
from . import models
from .serializer import PostSerializer
from django.db.models import Max, F, Q
from rest_framework.response import Response

# Create your views here.

def Home(request):
    return HttpResponse('hello welcome to nijablog backend')


class LatestPostViews(APIView):
    def get(self, request):
        posts = models.Article.objects.all().filter(is_published=True, post_file__type='Image').order_by('-created_at')[:5]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

class LatestNewViews(APIView):
    def get(self, request):
        News = models.Article.objects.all().filter(is_published=True, post_file__type="Image", cartegory="News").order_by('-created_at')[:5]
        serializer = PostSerializer(News, many=True)
        return Response(serializer.data)
    
class FeaturedVedioViews(APIView):
    def get(self, request):
        vedios = models.Article.objects.all().annotate(high=Max('reads')).filter(is_published=True, post_file__type="Video", reads=F('high'), tags__name='Featured').order_by('?')[:3]
        serializer = PostSerializer(vedios, many=True)
        return Response(serializer.data)

class PopularPostViews(APIView):
    def get(self, request):
        Popular_post = models.Article.objects.all().annotate(high=Max('reads')).filter(is_published=True, reads=F('high')).order_by('?')
        serializer = PostSerializer(Popular_post, many=True)
        return Response(serializer.data)