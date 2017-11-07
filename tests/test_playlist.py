import unittest
# Import class to be tested
from app.models import Playlist

class PlaylistTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Playlist class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_playlist = Playlist(name='banana')

    def test_instance(self):
        '''
        Test case to check if new_playlist is an instance of Playlist
        '''
        self.assertTrue( isinstance( self.new_playlist, Playlist))

    def test_save_playlist(self):
        '''
        Test case to check if a playlist is saved to the databse
        '''

        self.new_playlist.save_playlist()

        self.assertTrue( len(Playlist.query.all()) > 0 )

    def test_get_playlists(self):
        '''
        Test case to check if all playlists are returned by the get_playlists function
        '''

        self.new_playlist.save_playlist()

        test_playlist = Playlist(name="Product Pitches")

        test_playlist.save_playlist()

        gotten_playlists = Playlist.get_playlists()

        self.assertTrue( len(gotten_playlists) == len(Playlist.query.all()) )



