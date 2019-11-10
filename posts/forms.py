from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
        'id': 'username',
        'rows': '1'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'id': 'useremail',
        'rows': '1'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('user', 'email', 'content', )
