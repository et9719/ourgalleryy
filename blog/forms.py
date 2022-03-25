''' Imports '''''' Imports '''
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    ''' Add description '''
    class Meta:
        ''' Add Description '''
        # Model we want to use.
        model = Comment
        # What fields we want to use.
        fields = ('body',)
