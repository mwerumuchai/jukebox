from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Playlist

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    playlists = Playlist.get_playlists() 
    title = 'Home'

    return render_template('index.html', title = title, playlists = playlists)
   

