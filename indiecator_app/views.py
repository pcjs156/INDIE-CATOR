from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Artist
from .form import ArtistForm


# 아티스트 메인 페이지 : /artist
def artist_main(request):
    artists = Artist.objects.all()
    return render(request, 'artist_main.html', {'artists':artists})

# 아티스트 추가 페이지 : /artist/new
def new_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            return redirect('/artist/')

    else :
        form = ArtistForm()
        return render(request, 'new_artist.html', {'form':form})

# CRUD - Create : 구현은 나중에
def artist_create(request):
    pass

# 아티스트 수정 페이지 : /artist/edit/(artist_id)
def artist_edit(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            return redirect('/artist/')

    else :
        form = ArtistForm()
        return render(request, 'artist_edit.html', {'artist':artist, 'form':form})


# CRUD - Update : 구현은 나중에
def artist_update(request, artist_id):
    modified_artist = get_object_or_404(Artist)
    modified_artist.name = request.POST['name']
    modified_artist.debut_date = request.POST['debut_date']
    modified_artist.member = request.POST['member']
    modified_artist.description = request.POST['description']
    # modified_artist.profile_image = request.POST['profile_image']
    modified_artist.profile_image = request.POST.get('profile_image', False)

    modified_artist.save()
    
    return redirect('/artist/')


# CRUD - Delete : 구현은 나중에
def artist_delete(request, artist_id):
    pass