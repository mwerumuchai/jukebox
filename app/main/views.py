from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Playlist,Group,Song
from .forms import PlaylistForm
from flask_login import login_required,current_user
from .. import db,audios

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    playlists = Playlist.get_playlists() 
    title = 'Home'

    search_song = request.args.get('song_query')

    if search_song:
        return redirect(url_for('.search_song', song_name = search_song))
    else: 
        return render_template('index.html', title = title, playlists = playlists)

@main.route('/search/<song_name>')
def search_song(song_name):
    '''
    View function  for searching a song in the playlist
    '''
    found_songs = Song.search_songs(song_name)
    title = f'{song_name} results'
    return render_template('search.html', title = title, found_songs = found_songs)


@main.route('/playlist/<int:id>')
def playlist(id):
    '''
    View to display a specific playlist and its its songs
    '''

    playlist = Playlist.query.get(id)
    songs = Song.get_songs(id)

    songs_list = []
    for song in songs:
        songs_list.append(song.name)

    title = f'{playlist.name} page'

    return render_template('playlist.html', title=title, playlist=playlist, songs=songs, songs_list=songs_list )

@main.route('/group/<int:id>')
@login_required
def group(id):
    '''
    View group page function for the logged in group
    '''
    group = Group.query.get(id)
    playlists = Playlist.query.filter_by(group_id=id).all()

    if group is None:
        abort(404)
    
    if group.id != current_user.id:
        abort(403)

    title = f'{group.name} page'

    return render_template('group.html', title = title, group = group, playlists=playlists)

@main.route('/group/playlist/new/<int:id>', methods=['GET','POST'])
@login_required
def create_playlist(id):
    '''
    View create playsist function to display a form for creating a playlist
    '''

    group = Group.query.get(id)

    if group is None:
        abort(404)
    
    if group.id != current_user.id:
        abort(403)

    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data

        new_playlist = Playlist(name = name, group=group)
        new_playlist.save_playlist()
        return redirect(url_for('.group', id=group.id))

    title = f'New Playlist'

    return render_template('new_playlist.html', new_playlist_form=form)

@main.route('/group/playlist/<int:id>')
@login_required
def group_playlist(id):
    '''
    View function to display a specific playlist belonging to a specific group
    '''

    playlist = Playlist.query.get(id)
    songs = Song.get_songs(id)

    if playlist is None:
        abort(404)

    if playlist.group.id != current_user.id:
        abort(403)

    title = f'{playlist.name} page'

    return render_template('group_playlist.html', title=title, playlist=playlist, songs=songs)

@main.route('/group/playlist/song/new/<int:id>', methods=['GET','POST'])
@login_required
def new_song(id):
    '''
    View function to display a form for uploading a song
    '''
    playlist = Playlist.query.get(id)

    if playlist is None:
        abort(404)

    if playlist.group.id != current_user.id:
        abort(403)

    if 'audio' in request.files:

        filename = audios.save(request.files['audio'])
        path = f'audio/{filename}'
        song = Song(name=filename ,song_path=path, playlist=playlist)
        song.save_song()

        return redirect(url_for('main.group_playlist', id=playlist.id))

    return render_template('new_song.html', playlist=playlist)

@main.route('/group/playlist/song/delete/<int:id>')
@login_required
def delete_song(id):
    '''
    View function that deletes a song and redirect to the index view function
    '''
    song = Song.query.get(id)

    if song is None:
        abort(404)

    if song.playlist.group.id != current_user.id:
        abort(403)


    song.delete_song(id)

    return redirect(url_for('.group', id=current_user.id))

@main.route('/group/playlist/delete/<int:id>')
@login_required
def delete_playlist(id):
    '''
    View function that deletes a playlist and its songs and redirect to index view function
    '''
    playlist = Playlist.query.get(id)

    if playlist is None:
        abort(404)

    if playlist.group.id != current_user.id:
        abort(403)

    playlist.delete_playlist(id)

    return redirect(url_for('.group', id=current_user.id))



   

