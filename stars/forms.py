from django import forms
from .models import Star, ProfileImg, TagedImg

class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = '__all__'


class ProfileImgForm(forms.ModelForm):
    class Meta:
        model = ProfileImg
        fields = '__all__'


class TagedImgForm(forms.ModelForm):
    class Meta:
        model = TagedImg
        fields = '__all__'