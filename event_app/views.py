from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Event, Comment
from .form import CommentForm

# 사이트 전체 메인페이지
def main(request):
    return render(request, 'main.html')

# 이벤트 메인페이지 : /
def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events':events})

# 공연 세부 정보 : /event_det   ail/(event_id)
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    comments = Comment.objects.filter(event_id=event_id).order_by('-commented_date')
    form = CommentForm()

    response = {
        'event':event,
        'comments':comments,
        'form':form
    }

    return render(request, 'event_detail.html', response)

@login_required
def new_comment(request, event_id):
    new_comment = Comment()
    new_comment.event = get_object_or_404(Event, pk=event_id)
    new_comment.author = request.POST['author']
    new_comment.body = request.POST['body']
    new_comment.commented_date = timezone.datetime.now()
    new_comment.save()

    return redirect('/event/event_detail/' + str(event_id))