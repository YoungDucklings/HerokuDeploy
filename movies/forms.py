from django import forms
from accounts.models import Comment
from .models import Movie, Poster, Video, Backdrop

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'


class BackdropForm(forms.ModelForm):
    class Meta:
        model = Backdrop
        fields = '__all__'


class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = '__all__'