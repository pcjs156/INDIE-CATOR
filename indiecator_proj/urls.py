from django.contrib import admin
from django.urls import path, include
import indiecator_app.urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indiecator_app.views.home, name="home"),
    path('event_detail/<int:event_id>', indiecator_app.views.event_detail, name="event_detail"),
    path('artist/', include(indiecator_app.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
