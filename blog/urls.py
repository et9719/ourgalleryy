''' Imports '''
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('gallery/', views.PostList.as_view(), name='gallery'),
    path('news/', views.NewsPostList.as_view(), name='news'),
    path('add_news/', views.add_news, name='add_news'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_news/<slug:slug>/', views.edit_news, name='edit_news'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_news/<slug:slug>/', views.delete_news, name='delete_news'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('news/<slug:slug>/', views.NewsPostDetail.as_view(),
         name='news_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
]
