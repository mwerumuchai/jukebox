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
    image_path = db.Column(db.String())

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
    Playlist class to define a group in the database
    '''

    # Name of the table
    __tablename__ ='playlists'

    # id column that is the primary key
    id = db.Column(db.Integer,primary_key=True)

    # name column for the playlist name
    name = db.Column(db.String)

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
        '''
        playlists = Playlist.query.all()
        return playlists


