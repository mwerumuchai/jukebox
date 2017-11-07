from flask import render_template
from . import main

# Error handler decorator
@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    title = '404 page'
    return render_template('fourOwfour.html', title=title),404

# Error handler decorator
@main.app_errorhandler(403)
def four_Ow_three(error):
    '''
    Function to render the 403 error page
    '''
    title = '403 page'
    return render_template('fourOwthree.html', title=title),403