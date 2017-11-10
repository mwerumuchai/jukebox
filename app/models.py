from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(group_id):
    '''
    @login_manager.user_loader Passes in a group_id to this function
    Function queries the database and gets a group's id as a response
    '''
    return Group.query.get(int(group_id))

class Group(UserMixin,db.Model):
    '''
    Group class to define a group in the database
    '''

    # Name of the table
    __tablename__ = 'groups'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # name column for the group name
    name = db.Column(db.String)

    # password_hash column for passwords
    password_hash = db.Column(db.String(255))

    # description column for the group's description
    description = db.Column(db.String)

    # image_path column for the group's profile image
    image_path = db.Column(db.String)

    # relationship between group and playlist class
    playlists = db.relationship('Playlist', backref = 'group',lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class Playlist(db.Model):
    '''
    Playlist class to define a playlist in the database
    '''

    # Name of the table
    __tablename__ ='playlists'

    # id column that is the primary key
    id = db.Column(db.Integer,primary_key=True)

    # name column for the playlist name
    name = db.Column(db.String)

    # image_path column for the playlist's image
    image_path = db.Column(db.String)

    #group_id column for linking a playlist with a group
    group_id = db.Column(db.Integer,db.ForeignKey('groups.id')) 

    # relationship between playlist and song class
    songs = db.relationship('Song', backref = 'playlist',lazy = 'dynamic',  cascade="all, delete-orphan")


    def save_playlist(self):
        '''
        Function to save a playlist to the database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_playlists(cls):
        '''
        Function to retrieve playlists from database 

        Returns:
            playlists : list of playlists in the database
        '''
        playlists = Playlist.query.all()
        return playlists

    @classmethod
    def delete_playlist(cls,playlist_id):
        '''
        Function that deletes a specific playlist from the playlists table and database and also delete its songs

        Args:
            playlist_id : specific playlist id
        '''
        songs = Song.query.filter_by(playlist_id=playlist_id).delete()
        playlist = Playlist.query.filter_by(id=playlist_id).delete()
        db.session.commit()


class Song(db.Model):
    '''
    Song class to define a song in the database
    '''

    # Name of the table
    __tablename__ ='songs'

    # id column that is the primary key
    id = db.Column(db.Integer,primary_key=True)

    # name column for the name of the song
    name = db.Column(db.String)

    # song_path column for the path of the song
    song_path = db.Column(db.String)

    # playlist_id column for linking a song with a playlist
    playlist_id = db.Column(db.Integer,db.ForeignKey('playlists.id', ondelete='CASCADE')) 

    def save_song(self):
        '''
        Function to save a song to the database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_songs(cls,playlist_id):
        '''
        Function to retrieve songs from a specific playlist database

        Args:
            playlist_id : specific playlist id

        Returns:
            songs : list of songs belonging to the specific playlist
        '''
        songs = Song.query.filter_by(playlist_id= playlist_id).all()
        return songs
    
    @classmethod
    def delete_song(cls,song_id):
        '''
        Function to delete a song from the playlist 

        Args:
            song_id : specific id for a song 
        '''
        song = Song.query.filter_by(id=song_id).delete()
        db.session.commit()

    @classmethod
    def search_songs(cls,song_name):
        '''
        Function to search for a song in the database and return a list of matches

        Args:
            song_name : name of the song provided by the user

        Returns:
            songs : list of songs matching the song_name provided
        
        songs = []
        songs = [ Song.query.filter(Song.name.op('~')(r'\b{}\b'.format(keyword))).all() for keyword in list(song_name)]

        song_name_list = song_name.split(" ")
        song_name = "+".join(song_name_list)
        songs_found = []
        for keyword in song_name.split(' '):
            result = Song.query.filter(Song.name.op('~')(r'\b{}\b'.format(keyword))).all()
            songs_found.append(result)

        
        ''' 
        songs = Song.query.filter( Song.name.like(song_name+"%") ).all()
        songs_found = []
        for song in songs:
            songs_found.append(song.name)


        return songs_found




