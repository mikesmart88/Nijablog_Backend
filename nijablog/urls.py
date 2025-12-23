from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v

urlpatterns = [
    path('', v.Home, name="Homepage"),
    path('posts/general/type=latest/', v.LatestPostViews.as_view(), name="latest posts"),
    path('posts/news/type=latest/', v.LatestNewViews.as_view(), name='latest news'),
    path('posts/vedios/type=featured/', v.FeaturedVedioViews.as_view(), name='featured vedios'),
    path('posts/general/type=popular/', v.PopularPostViews.as_view(), name='popular posts'),
    path('posts/business/type=all/', v.BusinessPostViews.as_view(), name='Business posts'),
    path('posts/news/type=all/', v.NewsPostViews.as_view(), name='news post'),
    path('posts/sport/type=all/', v.SportPostViews.as_view(), name='sport post'),
    path('posts/biograph/type=all/', v.BiographPostViews.as_view(), name='biograph post'),
    path('posts/politic/type=all/', v.PoliticPostViews.as_view(), name='politics post'),
    path('posts/entertainment/type=all/', v.EntertainmentPostViews.as_view(), name='entertainment post'),
    path('posts/technology/type=all/', v.TechnologyPostViews.as_view(), name='tech post'),
    path('posts/finance/type=all/', v.FinancePostViews.as_view(), name='finance post'),
    path('posts/news/international/', v.InternationalNewsPostViews.as_view(), name='international news post'),
    
    path('posts/', v.PostListViews.as_view(), name='post list'),
]
