from django import forms
from . models import movie,review

class movieform(forms.ModelForm):
    class Meta:
         model=movie
         fields=['name','img','des','year','actors','category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ['user', 'comments', 'rating']

