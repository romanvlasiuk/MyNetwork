from django import forms
from .models import Publication, Comment, Photo
from datetime import datetime

class PublicationForm(forms.Form):

    article = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'span6'}) )
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'span6'}))

    def save(self,user):
        new = Publication()
        new.owner = user
        new.text = self.cleaned_data['text']
        new.article = self.cleaned_data['article']
        new.save()


class AddCommentForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea(attrs={'class':'span6'}))

    def save(self, publication, user):
        new = Comment()
        new.publication = publication
        new.author = user
        new.time = datetime.now()
        new.text = self.cleaned_data['text']
        new.save()


class AddPhotoForm(forms.Form):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'span6'}))
    photo = forms.ImageField()

    def save(self, user):
        new = Photo()
        new.owner = user
        new.title = self.cleaned_data['title']
        new.image = self.cleaned_data['photo']
        new.save()
