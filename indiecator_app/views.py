from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Max

from .models import Artist
from .form import ArtistForm


# 아티스트 메인 페이지 : /artist
def artist_main(request):
    artists = Artist.objects.all()

    top_interest = artists.aggregate(Max('interest'))['interest__max']
    
    top_artists = artists.filter(interest=top_interest).order_by('name')
    rest_artists = artists.exclude(interest=top_interest).order_by('-interest')
    

    return render(request, 'artist_main.html', {'top_artists':top_artists, 'rest_artists':rest_artists})

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


# CRUD - Update
def artist_update(request, artist_id):
    modified_artist = get_object_or_404(Artist, pk=artist_id)
    modified_artist.name = request.POST['name']
    modified_artist.debut_date = request.POST['debut_date']
    modified_artist.member = request.POST['member']
    modified_artist.description = request.POST['description']
    # modified_artist.profile_image = request.POST['profile_image']
    modified_artist.profile_image = request.POST.get('profile_image', False)

    modified_artist.save() 
    
    return redirect('/artist/')


# CRUD - Delete
def artist_delete(request, artist_id):
    target_artist = get_object_or_404(Artist, pk=artist_id)
    target_artist.delete()
    return redirect('artist_main')

def interest_up(request, artist_id):
    target_artist = get_object_or_404(Artist, pk=artist_id)
    print(target_artist.interest)
    target_artist.interest += 1
    target_artist.save()

    return redirect('/artist' + '#' + str(artist_id))