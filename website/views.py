from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from game_classes.player import Player

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """
    If the user is logged in, show the home page

    :return: The home html template
    """

    if request.method == 'POST':

    return render_template("home.html", user=current_user, msg=msg)


@views.route('/scoreboard')
@login_required
def scoreboard():
    """
    If the user is logged in, show the scoreboard

    :return: The scoreboard html template
    """
    return render_template("scoreboard.html", user=current_user)
