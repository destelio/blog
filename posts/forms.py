from django import forms

from .models import Post, Comment

from django.contrib.auth import get_user_model 
User = get_user_model() 



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')




class CommentForm(forms.ModelForm):
    content = forms.CharField(required= True,    widget = forms.Textarea (attrs={'rows':4}))
    class Meta:
        model = Comment
        fields = ('content',)