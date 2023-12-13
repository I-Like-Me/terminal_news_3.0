from datetime import datetime, timezone
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
import sqlalchemy as sa
from app import db
from app.models import User
from app.main.forms import PickTopics

from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    content = {'food': 'Pizza'}
    form = PickTopics()
    return render_template('index.html', title='Home', content=content, form=form)