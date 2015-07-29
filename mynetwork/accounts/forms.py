from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class':'span4'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'span4'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'span4'})


class ProfileRegistrationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('birthday', 'about', 'photo')

    def __init__(self, *args, **kwargs):
        super(ProfileRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['about'].widget = forms.Textarea(attrs={'class':'span4'})


class ProfileEditionForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'span6'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'span6'}))
    birthday = forms.DateField()
    email = forms.EmailField()
    about = forms.CharField(widget=forms.Textarea(attrs={'class':'span6'}))
    photo = forms.ImageField()

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        profile = user.profile
        profile.birthday = self.cleaned_data['birthday']
        profile.about = self.cleaned_data['about']
        profile.photo = self.cleaned_data['photo']
        profile.save()