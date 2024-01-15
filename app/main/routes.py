from datetime import datetime, timezone
from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_required
from app import db
from app.models import User, Character, Folder
from app.main.forms import PickNPCs, PickTopics, AssetSel, LoginForm
from app.main.toolbox import Converters, Collectors, Builders
from app.main import bp
import markdown




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

@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@bp.route('/viewer/<catagory>/<asset>', methods=["POST", "GET"])
def asset_view(catagory, asset):
    
    cata = catagory
    asset_item = asset
    
    return render_template('asset_viewer.html', cata=cata, asset_item=asset_item)

@bp.route('/article', methods=["POST", "GET"])
def article():
    
    data = {}
    data["page_title"] = "Article"

    with open('/Users/cass/Documents/python/story_keeper/terminal_news_3.0/app/main/content/article.md', 'r') as f:
        text = f.read()
        data["html"] = markdown.markdown(text)
    
    
    return render_template('article.html', data=data)

@bp.route('/asset_sel', methods=["POST", "GET"])
def asset_sel():
    form = AssetSel()
    if form.validate_on_submit():
        type = request.form.get('asset_type')
        #return redirect(f'/adder/{type}') 
        return redirect(url_for('main.adder', asset=type))
    return render_template('gm_tools/selectors/asset_sel.html', title='Home', form=form)

@bp.route('/adder/<asset>', methods=["POST", "GET"])
def adder(asset):
    if asset == 'Character':
        # return redirect(f'/create_char/{asset}')
        return redirect(url_for('main.create_char', asset=asset))
    asset_form = Converters.str_to_class(f'{asset}Form')()
    asset_items = Collectors.get_bin(asset)
    if asset_items is not None:
        for x, y in asset_items.items():
            asset_form[x].query = Converters.str_to_class(y).query.all()
    if asset_form.validate_on_submit():
        new_asset = Builders.build_commit(asset, asset_form.data, asset_items)
        db.session.add(new_asset)
        db.session.commit()
        # return redirect(f'/adder/{asset}')
        return redirect(url_for('main.adder', asset=asset))
    return render_template(f'gm_tools/adders/{asset}_adder.html', title='Home', asset_form=asset_form)

@bp.route('/create_char/<asset>', methods=["POST", "GET"])
def create_char(asset):
    asset_form = Converters.str_to_class(f'{asset}Form')()
    asset_items = Collectors.get_bin(asset)
    if asset_items is not None:
        for x, y in asset_items.items():
            asset_form[x].query = Converters.str_to_class(y).query.all()
    return render_template(f'gm_tools/adders/character_adder.html', title='Home', asset_form=asset_form)


@bp.route('/filing/<path>', methods=["POST", "GET"])
def filing(path):
    url_path = path
    structure_dict = {}
    par_left2index = []
    temp_chi_left2index = []
    all_chi_left2index = []
    root_folder = Folder.query.filter_by(name='root').first()
    order = Builders.build_structure(root_folder)
    # for folder in root_folder.children_dirs:
    #     par_left2index.append(folder)
    #     structure_dict[folder] = {}
    #while len(temp_chi_left2index) != 0 and len(par_left2index) != 0:
    # for par in par_left2index:
    #     for par_chi in par.children_dirs:
    #         temp_chi_left2index.append(par_chi)
  
    return render_template(f'filing_cabinet.html', url_path=url_path, root_folder=root_folder, order=order)