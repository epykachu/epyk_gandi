from flask import Blueprint, render_template_string
from epyk.core.Page import Report


welcome = Blueprint('welcome', __name__)

@welcome.route('/')
def welcome_route():
    """Splash Page"""
    page = Report()
    page.ui.title('Welcome to Code Betas')
    return render_template_string(page.outs.html()), 200