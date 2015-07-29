from datetime import datetime
from django import forms
from models import Message


class NewMessageForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'span6'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'span6'}))

    def save(self, author, reciever):
        new = Message()
        new.user1 = author
        new.user2 = reciever
        new.time = datetime.now()
        new.title = self.cleaned_data['title']
        new.text = self.cleaned_data['text']
        new.save()