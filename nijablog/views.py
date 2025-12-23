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

class BusinessPostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='Business', tags__name='Finance').filter(tags__name='Analytics').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class NewsPostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='News').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class SportPostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='Sport').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class BiographPostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='Biograph').filter(tags__name='History').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class PoliticPostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='Politics').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class EntertainmentPostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='Entertainments').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class TechnologyPostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='Technology').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class FinancePostViews(APIView):
    def get(self, request):
        Posts = models.Article.objects.all().filter(is_published=True, cartegory='Finance').filter(tags__name='Money').order_by('?')
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)
    
class InternationalNewsPostViews(APIView):
    def get(self, request):
        country = request.query_params.get('country', '').strip()
        Posts = models.Article.objects.filter(
            is_published=True,
            cartegory='News'
        )
        if country:
            Posts = Posts.exclude(region__name__iexact=country)

        serializer = PostSerializer(Posts.order_by('?'), many=True)
        print('country:',country)
        return Response(serializer.data)
    


class PostListViews(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        post_type = request.query_params.get('type')
        region = request.query_params.get('country')

        Posts = models.Article.objects.filter(is_published=True)

        # Category filter
        if category and category != 'general':
            Posts = Posts.filter(cartegory=category)

        # Region filter
        if region and region != 'all':
            Posts = Posts.filter(region__name__iexact=region)

        if post_type == 'latest':
            Posts = Posts.order_by('-created_at')

        elif post_type == 'popular':
            Posts = Posts.order_by('-reads')

        else:
            Posts = Posts.order_by('?')


        #Posts = Posts.order_by('?')

        serializer = PostSerializer(Posts, many=True)
        print('category:', category, 'type:', post_type, 'region:', region)
        return Response(serializer.data)



