from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import ProfileRegistrationForm, ProfileEditionForm, MyUserCreationForm
from .models import UserProfile


def registrate(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        form_profile = ProfileRegistrationForm(request.POST, request.FILES)
        if form.is_valid() and form_profile.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user and user.is_active:
                    auth.login(request, user)
                    profile = UserProfile(user=user, birthday=form_profile.cleaned_data['birthday'],
                                          about=form_profile.cleaned_data['about'],
                                          photo=request.FILES['photo'])
                    profile.save()
                    return HttpResponseRedirect('/main/')
            else:
                return render(request, 'registration.html', {'form_user': form,
                                                             'form_profile': form_profile})
        else:
            return render(request, 'registration.html', {'form_user': form,
                                                         'form_profile': form_profile})
    else:
        form = MyUserCreationForm()
        form_profile = ProfileRegistrationForm()
        return render(request, 'registration.html', {'form_user': form,
                                                     'form_profile': form_profile})


def edit_profile(request):

    form = ProfileEditionForm()
    user = User.objects.get(id=request.session['current_user'])
    content = {'user': user, 'profile': user.profile, 'publications': user.publications,
                    'amount': user.pub_amount, 'root' : request.user,'form': form}

    if request.method == 'POST':
        form = ProfileEditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect('/main/display/')
        else:
            return render(request, 'profile_edit.html', content)
    else:
        return render(request, 'profile_edit.html', content)