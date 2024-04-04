import json

class JsonTools:

    def find_path(json_obj, value, repr_p, path=()):
        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                if k == 'name':
                    v_name = v
                new_path = JsonTools.find_path(v, value, repr_p + (v_name,), path + (k,))
                if new_path is not None:
                    return new_path
        elif isinstance(json_obj, list):
            for i, v in enumerate(json_obj):
                new_path = JsonTools.find_path(v, value, repr_p + (' > ',), path + (i,))
                if new_path is not None:
                    return new_path
        elif json_obj == value:
            return path, repr_p

    def find_repr_path(json_obj, value, path=()):
        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                new_path = JsonTools.find_path(v, value, path + (v,))
                if new_path is not None:
                    return new_path
        elif isinstance(json_obj, list):
            for i, v in enumerate(json_obj):
                new_path = JsonTools.find_path(v, value, path + (i,))
                if new_path is not None:
                    return new_path
        elif json_obj == value:
            return path

    def path_to_string(path):
        return json.dumps(path)
    
    def path_to_repr_string(path):
        path_list = list(path)
        path_string = path_list.pop(0)
        for item in path_list:
            path_string = path_string + f' > {item}'

    def string_to_path(path_string):
        return json.loads(path_string)
    
    def get_value_by_path(json_obj, path):
        for key in path:
            if isinstance(key, int):
                json_obj = json_obj[key]
            else:
                json_obj = json_obj.get(key)
        return json_obj
    
    def replace_value_by_path(json_obj, path, new_value):
        *path, last_key = path
        for key in path:
            if isinstance(key, int):
                json_obj = json_obj[key]
            else:
                json_obj = json_obj.get(key)
        if isinstance(last_key, int):
            json_obj[last_key] = new_value
        else:
            json_obj[last_key] = new_value