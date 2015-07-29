from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'authorization.html'}),
    url(r'/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'/registration/$', 'accounts.views.registrate'),
    url(r'/edit_profile/$', 'accounts.views.edit_profile'),
]
