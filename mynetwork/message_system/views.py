from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from forms import NewMessageForm
from models import Message


def inbox(request):
    user = request.user
    messages = user.get_messages
    return render(request, 'show_inbox_messages.html', content_creator(request, user, messages=messages))


def outbox(request):
    user = request.user
    messages = user.sent_messages
    return render(request, 'show_outbox_messages.html', content_creator(request, user, messages=messages))


def new_message(request):
    user = User.objects.get(id=request.session['current_user'])
    form = NewMessageForm()
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            form.save(request.user, user)
            return HttpResponseRedirect('/main/display/')
        else:
            return render(request, 'add_message.html', content_creator(request, user, form=form))
    else:
        return render(request, 'add_message.html', content_creator(request, user, form=form))


def show_message(request):
    id = request.GET['id']
    print id
    show_button = request.GET['button']
    message = Message.objects.get(id=id)
    print message
    request.session['current_user'] = message.user1.id
    return render(request, 'show_message.html', content_creator(request, request.user,
                                                                message=message, show_button=show_button))


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
    if 'messages' in kwargs:
        content['messages'] = kwargs['messages']
    if 'message' in kwargs:
        content['message'] = kwargs['message']
    if 'show_button' in kwargs:
        content['show_button'] = kwargs['show_button']
    return content