from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from game_classes.game import Game
from . import db
from .models import TimeRecord

views = Blueprint('views', __name__)
game = Game()


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """
    If the user is logged in, show the home page. The home page is where the
    user will play the game. Display text in response to player commands.

    :return: The home html template
    """

    messages = []
    player_status = game.display_player_status()
    outcome = ''

    if request.method == 'GET':
        messages.append(game.display_opening_message())

    if request.method == "POST":
        command = request.form.get('command', '')
        if command:
            if game.start_time is None:
                game.start_timer()
            result = game.process_command(command)
            messages.append(result)
            messages.append(game.display_room_status(
                game.player.current_room.name))
            player_status = game.display_player_status()
            outcome = game.player_outcome()

            if outcome == 'won':
                elapsed_time = game.get_elapsed_time()
                messages.append(game.WINNING_MESSAGE)
                try:
                    new_record = TimeRecord(user_id=current_user.id,
                                            date=game.end_time,
                                            elapsed_time=elapsed_time)
                    db.session.add(new_record)
                    db.session.commit()
                except Exception as e:
                    print(f"Error adding time record: {e}")
            elif outcome == 'lost':
                messages.append(game.LOSING_MESSAGE)

    return render_template(
        "home.html",
        user=current_user,
        messages=messages,
        player_status=player_status,
        outcome=outcome
    )


@views.route('/reset')
def reset_game():
    """
    Reset any progress and start the game over from the beginning.

    :return: A redirect to the home page with game data reset
    """
    global game
    game = Game()
    return redirect(url_for('views.home'))


@views.route('/scoreboard')
@login_required
def scoreboard():
    """
    If the user is logged in, show the scoreboard

    :return: The scoreboard html template
    """
    records = TimeRecord.query.filter_by(user_id=current_user.id) \
        .order_by(TimeRecord.elapsed_time).all()
    return render_template("scoreboard.html", user=current_user,
                           records=records)
