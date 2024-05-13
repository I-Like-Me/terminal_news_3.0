from datetime import datetime, timezone
from flask import render_template, flash, redirect, url_for, request, g, current_app, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import User, Character, File, Ability, Skill, Damagetype
from app.auth.forms import LoginForm
from app.main.forms import PickNPCs, PickTopics, AssetSel
from app.main.toolbox import Converters, Collectors, Builders, Organizer, JsonTools
from app.main import bp
import markdown
from collections import OrderedDict


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

@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('user.html', user=user)

@bp.route('/viewer/<catagory>/<asset>', methods=["POST", "GET"])
@login_required
def asset_view(catagory, asset):
    
    cata = catagory
    asset_item = asset
    
    return render_template('asset_viewer.html', cata=cata, asset_item=asset_item)

@bp.route('/article', methods=["POST", "GET"])
@login_required
def article():
    
    data = {}
    data["page_title"] = "Article"

    with open('/Users/cass/Documents/python/story_keeper/terminal_news_3.0/app/main/content/article.md', 'r') as f:
        text = f.read()
        data["html"] = markdown.markdown(text)
    
    
    return render_template('article.html', data=data)

@bp.route('/asset_sel', methods=["POST", "GET"])
@login_required
def asset_sel():
    form = AssetSel()
    if form.validate_on_submit():
        type = request.form.get('asset_type')
        #return redirect(f'/adder/{type}') 
        return redirect(url_for('main.adder', asset=type))
    return render_template('gm_tools/selectors/asset_sel.html', title='Home', form=form)

@bp.route('/adder/<asset>', methods=["POST", "GET"])
@login_required
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
@login_required
def create_char(asset):
    asset_form = Converters.str_to_class(f'{asset}Form')()
    asset_items = Collectors.get_bin(asset)
    if asset_items is not None:
        for x, y in asset_items.items():
            asset_form[x].query = Converters.str_to_class(y).query.all()
    return render_template(f'gm_tools/adders/character_adder.html', title='Home', asset_form=asset_form)

@bp.route('/filing/<username>', methods=["POST", "GET"])
@login_required
def filing(username):
    user = User.query.filter_by(username=username).first_or_404()
    print(user.my_documents)
    return render_template('filing_cabinet.html', user_name=user.username)

@bp.route('/process_file_content', methods=['POST'])
def process_file_content():
    content = request.json['content']
    file = Collectors.get_file(content)
    return jsonify(processed_content=file.content)

@bp.route('/get_cabinet/<username>', methods=['GET'])
def get_cabinet(username):
    user = User.query.filter_by(username=username).first_or_404()
    return jsonify(user.my_documents)

@bp.route('/save_content', methods=['POST'])
def save_content():
    data = request.get_json()
    new_content = data['content']
    desired_file = Collectors.get_file(data['f_id'])
    desired_file.content = new_content
    db.session.commit()
    return 'Success!', 200

@bp.route('/get_categories', methods=['GET'])
def get_categories():
    return {1: 'Ability', 2: 'Skill', 3: 'Damage Type'}

@bp.route('/get_category/<string:category>', methods=['GET'])
def get_category(category):
    if category == 'Ability':
        entries = Ability.query.all()
    elif category == 'Skill':
        entries = Skill.query.all()
    elif category == 'Damage Type':
        entries = Damagetype.query.all()
    return {entry.id: entry.name for entry in entries}

@bp.route('/get_ability/<int:id>', methods=['GET'])
def get_ability(id):
    ability = Ability.query.get(id)
    return {'name': ability.name}

@bp.route('/get_skill/<int:id>', methods=['GET'])
def get_skill(id):
    skill = Skill.query.get(id)
    return {'name': skill.name}

@bp.route('/get_damage_type/<int:id>', methods=['GET'])
def get_damage_type(id):
    damagetype = Damagetype.query.get(id)
    return {'name': damagetype.name}

@bp.route('/get_summary', methods=['POST'])
def get_summary():
    data = request.get_json()
    print(data['entryNameK'])
    return jsonify(data['entryNameK'])

@bp.route('/update_json', methods=['POST'])
def update_json():
    data = request.get_json()
    order = ['name', 'type', 'content', 'children']
    ready_data = Organizer.reorder_keys(data['updatedJSON'], order)
    user = User.query.filter_by(username=data['author']).first_or_404()
    print(f"The Author is {data['author']}")
    print(f"The name of the selected item is {data['selItemName']}")
    print(f"The type of the selected item is {data['selItemType']}")
    print(f"The type of the selected item is {data['selItemContent']}")
    print(f"The item being affected is {data['itemName']}")
    print(f"The item type being affected is {data['itemType']}")
    print(f"The repr path to the item being affected is {data['changeLocation']}")
    print(f"The parent of the item being affected is {data['parentName']}")
    print(f"The files that need to be checked are {data['fileList']}")
    print(f"The files to delete are {data['changeList']}")
    print(f"The location of the affected item's parent is {data['parentLocation']}") 
    print(f"The action being taken is {data['action']}")
    print(f"The list of files include {data['allFiles']}")
    print(data['moveSourcePath'])
    print(data['moveDestinationPath'])
    if data['action'] == 'add':
        JsonTools.sort_nested_list(ready_data['children'])
        if data['itemType'] == 'folder':
            if len(data['allFiles']) > 0:
                for f_id in data['allFiles']:
                    cur_file = Collectors.get_file(f_id)
                    filePath = JsonTools.find_path(ready_data, f_id, path=())
                    filePathString = JsonTools.path_to_string(filePath)
                    reprFilePath = JsonTools.build_repr_from_path(ready_data, filePath)
                    reprFileString = JsonTools.repr_path_to_string(reprFilePath)
                    cur_file.access_path = filePathString
                    cur_file.repr_path = reprFileString
                    db.session.commit()            
            user.my_documents = ready_data
            db.session.commit()
        if data['itemType'] == 'file':
            pathTuple = JsonTools.find_path(ready_data, 'Type Here', path=())
            pathString = JsonTools.path_to_string(pathTuple)
            reprPath = JsonTools.build_repr_from_path(ready_data, pathTuple)
            reprString = JsonTools.repr_path_to_string(reprPath)
            data['allFiles'].remove('Type Here')
            if len(data['allFiles']) > 0:
                for f_id in data['allFiles']:
                    cur_file = Collectors.get_file(f_id)
                    filePath = JsonTools.find_path(ready_data, f_id, path=())
                    filePathString = JsonTools.path_to_string(filePath)
                    reprFilePath = JsonTools.build_repr_from_path(ready_data, filePath)
                    reprFileString = JsonTools.repr_path_to_string(reprFilePath)
                    cur_file.access_path = filePathString
                    cur_file.repr_path = reprFileString
                    db.session.commit()
            new_file = File(name=data['itemName'], author=data['author'], repr_path=reprString, access_path=pathString, content='Type Here')
            db.session.add(new_file)
            db.session.commit()
            JsonTools.update_nested_dict(ready_data, pathTuple, new_file.id)
            user.my_documents = ready_data
            db.session.commit()
    if data['action'] == 'delete':
        JsonTools.sort_nested_list(ready_data['children'])
        final_affected_list = []
        for f_id in data['allFiles']:
            if f_id not in data['changeList']:
                final_affected_list.append(f_id)
        print(final_affected_list)
        user.my_documents = ready_data
        if len(data['changeList']) > 0:
            for item in data['changeList']:
                file_to_delete = File.query.get(item)
                if file_to_delete is not None:
                    db.session.delete(file_to_delete)
        db.session.commit()
        if len(final_affected_list) > 0:
            for f_id in final_affected_list:
                cur_file = Collectors.get_file(f_id)
                filePath = JsonTools.find_path(ready_data, f_id, path=())
                filePathString = JsonTools.path_to_string(filePath)
                reprFilePath = JsonTools.build_repr_from_path(ready_data, filePath)
                reprFileString = JsonTools.repr_path_to_string(reprFilePath)
                cur_file.access_path = filePathString
                cur_file.repr_path = reprFileString
                db.session.commit()
    if data['action'] == 'move':
        JsonTools.add_to_nested_dict(ready_data, data['moveSourcePath'], data['moveDestinationPath'])
        JsonTools.sort_nested_list(ready_data['children'])
        user.my_documents = ready_data
        db.session.commit()
        if len(data['allFiles']) > 0:
            for f_id in data['allFiles']:
                cur_file = Collectors.get_file(f_id)
                filePath = JsonTools.find_path(ready_data, f_id, path=())
                filePathString = JsonTools.path_to_string(filePath)
                reprFilePath = JsonTools.build_repr_from_path(ready_data, filePath)
                reprFileString = JsonTools.repr_path_to_string(reprFilePath)
                cur_file.access_path = filePathString
                cur_file.repr_path = reprFileString
                db.session.commit()
    return jsonify(user.my_documents)


  