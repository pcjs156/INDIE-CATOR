from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="event_home"),
    path('#event_list', views.home, name="event_list"),
    path('event_detail/<int:event_id>', views.event_detail, name="event_detail"),
    path('new_comment/<int:event_id>', views.new_comment, name="new_comment"),
]