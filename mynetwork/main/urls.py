from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^/$', 'main.views.main'),
    url(r'^/open/', 'main.views.open'),
    url(r'^/add_pub/', 'main.views.add_pub'),
    url(r'^/authors/', 'main.views.show_authors'),
    url(r'^/author/', 'main.views.show_author'),
    url(r'^/display/', 'main.views.display'),
    url(r'^/add_comment/', 'main.views.add_comment'),
    url(r'^/photo/', 'main.views.show_photo'),
    url(r'^/add_photo/', 'main.views.add_photo'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
