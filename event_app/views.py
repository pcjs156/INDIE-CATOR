from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Comment

# 메인 페이지 : /
def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events':events})

# 공연 세부 정보 : /event_detail/(event_id)
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    comments = Comment.objects.filter(event_id=event_id)

    return render(request, 'event_detail.html', {'event':event, 'comments':comments})
