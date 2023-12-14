from datetime import datetime, timezone
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User, Character
from app.main.forms import PickNPCs, PickTopics

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