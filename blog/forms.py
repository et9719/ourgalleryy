''' Imports '''
from django import forms
from .models import Comment, NewsPost, Post


class CommentForm(forms.ModelForm):
    ''' Form to allow user to add comment '''
    class Meta:
        ''' model used and field used '''
        # Model we want to use.
        model = Comment
        # What fields we want to use.
        fields = ('body',)


class NewsForm(forms.ModelForm):
    ''' Form to allow admin to add new newspost '''
    class Meta:
        ''' model used and field used '''
        # Model we want to use.
        model = NewsPost
        # What fields we want to use.
        fields = (
            'title',
            'description',
            'content',
            'featured_image',
            'excerpt',
            'status'
        )


class PostForm(forms.ModelForm):
    ''' Form to allow users to add new post '''
    class Meta:
        ''' model used and field used '''
        # Model we want to use.
        model = Post
        # What fields we want to use.
        fields = (
            'title',
            'content',
            'featured_image',
            'excerpt',
            'status'
        )
