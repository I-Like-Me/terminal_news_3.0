from flask import render_template
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    content = {'food': 'Pizza'}
    return render_template('index.html', title='Home', content=content)