from django.contrib import admin
from django.urls import path, include, re_path
from . import views as v

urlpatterns = [
    path('', v.Home, name="Homepage"),
    path('posts/general/type=latest/', v.LatestPostViews.as_view(), name="lestes posts"),
    path('posts/news/type=latest/', v.LatestNewViews.as_view(), name='latest news'),
    path('posts/vedios/type=featured/', v.FeaturedVedioViews.as_view(), name='featured vedios'),
    path('posts/general/type=popular/', v.PopularPostViews.as_view(), name='popular posts'),
]
