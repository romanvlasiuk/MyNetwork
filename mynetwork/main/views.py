from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Publication
from .forms import PublicationForm, AddCommentForm, AddPhotoForm


def main(request):
    user = request.user
    request.session[ 'root_user' ] = user.id
    request.session[ 'current_user' ] = user.id
    if user.publications:
        request.session[ 'current_pub' ] = user.publications[0].id
    else:
        request.session[ 'current_pub' ] = None
    return HttpResponseRedirect('/main/display/')


def open(request):
    request.session[ 'current_pub' ] = request.GET['id']
    return HttpResponseRedirect('/main/display/')


def add_pub(request):
    form = PublicationForm()
    user = request.user
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save(user)
            return HttpResponseRedirect('/main/')
        else:
            return render(request, 'add_pub.html', content_creator(request, user, form=form))
    else:
        return render(request, 'add_pub.html', content_creator(request, user, form=form))


def add_comment(request):
    form = AddCommentForm()
    user = User.objects.get(id=request.session['current_user'])
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            pub = Publication.objects.get(id=request.session['current_pub'])
            form.save(pub, request.user)
            return HttpResponseRedirect('/main/display/')
        else:
            return render(request, 'add_comment.html', content_creator(request, user, form=form))
    else:
        return render(request, 'add_comment.html', content_creator(request, user, form=form))


def show_authors(request):
    user = request.user
    authors = User.objects.all()
    return render(request, "authors.html", content_creator(request, user, authors=authors))


def show_author(request):
    user = User.objects.get(id=request.GET['id'])
    request.session['current_user'] = user.id

    if user.publications:
        request.session['current_pub'] = user.publications[0].id
    else:
        request.session['current_pub'] = None
    return HttpResponseRedirect('/main/display/')


def display(request):
    user = User.objects.get(id=request.session['current_user'])
    if request.session['current_pub']:
        current_publication = Publication.objects.get(id=request.session['current_pub'])
    else:
        current_publication = None
    return render(request, 'main.html', content_creator(request, user,
                                                        curent_publication=current_publication))


def show_photo(request):
    user = User.objects.get(id=request.session['current_user'])
    return render(request, 'photo.html', content_creator(request, user))


def add_photo(request):
    form = AddPhotoForm()
    user = User.objects.get(id=request.session['current_user'])
    if request.method == 'POST':
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect('/main/photo/')
        else:
            return render(request, 'add_photo.html', content_creator(request, user, form=form))
    else:
        return render(request, 'add_photo.html', content_creator(request, user, form=form))


def content_creator(request, user, **kwargs):
    user = user
    content = {'user': user,
               'profile': user.profile,
               'publications': user.publications,
               'amount': user.pub_amount,
               'root' : request.user,
               }
    if 'form' in kwargs:
        content['form'] = kwargs['form']
    if 'curent_publication' in kwargs:
        content['curent_publication'] = kwargs['curent_publication']
    if 'authors' in kwargs:
        content['authors'] = kwargs['authors']
    return content