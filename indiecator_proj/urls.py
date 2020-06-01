from django.contrib import admin
from django.urls import path, include

import indiecator_app.urls
import event_app.urls
import accounts.urls

import event_app.views as ev

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_app.views.main, name="main"),
    path('/event#event_list', ev.event_list, name="event_list"),
    path('event/', include(event_app.urls)),
    path('artist/', include(indiecator_app.urls)),
    path('accounts/', include(accounts.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
