from datetime import datetime, timezone
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User, Character
from app.main.forms import PickNPCs, PickTopics, AssetSel

from app.main import bp


@bp.route('/', methods=["POST", "GET"])
@bp.route('/index', methods=["POST", "GET"])
def index():
    content = {'food': 'Pizza'}
    npc_form = PickNPCs()
    npc_form.npcs.query = Character.query.filter_by(npc=True)
    if npc_form.validate_on_submit():
        print(npc_form.npcs.data)

    learner = Character.query.filter_by(name='Bort').first()
    sub_topics = learner.check_all_topics('Rosc')
    preselect = []
    for k, v in sub_topics.items():
        if v is True:
            preselect.append(k)
    topic_form = PickTopics(topics = preselect)

    if topic_form.validate_on_submit():
        print(topic_form.topics.data)

    return render_template('index.html', title='Home', content=content, npc_form=npc_form, topic_form=topic_form, preselect=preselect)

@bp.route('/asset_sel')
def asset_sel():
    form = AssetSel()
    if form.validate_on_submit():
        username = request.form.get('username')
        user = User.query.filter_by(username=username.lower()).first()
        if user is None:
            return redirect(url_for('auth.login'))
        try:
            duo_client.health_check()
        except DuoException:
            traceback.print_exc()
            if Config.duo_failmode.upper() == "OPEN":
                return render_template("auth/login.html", message="Login 'Successful', 2FA Not Performed.")
            else:
                return render_template("auth/login.html", message="2FA Unavailable.")
        state = duo_client.generate_state()
        session['state'] = state
        session['username'] = username.lower()
        prompt_uri = duo_client.create_auth_url(username.lower(), state)
        return redirect(prompt_uri)
    return render_template('asset_sel.html', title='Home')

@bp.route('/adder/<asset>', methods=["POST", "GET"])
def adder(asset):


    return render_template(f'{asset}_adder.html', title='Home')