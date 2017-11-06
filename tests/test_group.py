import unittest
# Import class to be tested
from app.models import Group

class GroupTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Group class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_group = Group(password='banana')

    def test_instance(self):
        '''
        Test case to check if new_group is an instance of Group
        '''
        self.assertTrue( isinstance( self.new_group, Group))

    def test_password_setter(self):
        '''
        Test case to ascertain when a password is being hashed and pass_secure contains a value
        '''
        self.assertTrue(self.new_group.password_hash is not None)

    def test_no_access_password(self):
        '''
        Test case to confirm the application raises an AttributeError when we try to access the password property
        '''
        with self.assertRaises(AttributeError):
            self.new_group.password

    def test_password_verification(self):
        '''
        Test case that confirms that our group password_hash can be verified when we pass in the correct the password
        '''
        self.assertTrue(self.new_group.verify_password('banana'))


