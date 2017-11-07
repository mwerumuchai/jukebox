from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PlaylistForm(FlaskForm):
    '''
    Class to create wtf for creating a playlist
    '''
    name = StringField('Playlist Name', validators = [Required()])
    submit = SubmitField('Submit')
