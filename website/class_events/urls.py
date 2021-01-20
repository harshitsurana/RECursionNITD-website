from django.urls import path
from .views import *
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

app_name="class_events"
urlpatterns=[
    path('create/event/', revent_create, name='revent_create'),
    path('create/class/', class_create, name='class_create'),
    path('update/class/<int:id>/', class_update, name='class_update'),
    path('update/event/<int:id>/', revent_update, name='revent_update'),
    path('detail/event/<int:id>/', revent_detail, name='revent_detail'),
    path('detail/class/<int:id>/', class_detail, name='class_detail'),
    path('',events, name='events'),
    url(r'^markdownx/', include('markdownx.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
