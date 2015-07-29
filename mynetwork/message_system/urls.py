from django.conf.urls import url


urlpatterns = [
    url(r'/inbox/$', 'message_system.views.inbox'),
    url(r'/outbox/$', 'message_system.views.outbox'),
    url(r'/message/$', 'message_system.views.show_message'),
    url(r'/new/$', 'message_system.views.new_message'),
]