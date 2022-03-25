''' Imports '''
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('gallery/', views.PostList.as_view(), name='gallery'),
    path('news/', views.NewsPostList.as_view(), name='news'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('news/<slug:slug>/', views.NewsPostDetail.as_view(),
         name='news_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
