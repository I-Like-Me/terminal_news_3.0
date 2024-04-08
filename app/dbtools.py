import json

class JsonTools:

    def find_path(json_obj, value, path=()):
        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                new_path = JsonTools.find_path(v, value, path + (k,))
                if new_path is not None:
                    return new_path
        elif isinstance(json_obj, list):
            for i, v in enumerate(json_obj):
                new_path = JsonTools.find_path(v, value, path + (i,))
                if new_path is not None:
                    return new_path
        elif json_obj == value:
            return path
        
    def build_repr_from_path(json_obj, path):
        repr_path = []
        for key in path:
            if isinstance(key, int):
                json_obj = json_obj[key]
                repr_path.append(' > ')
            else:
                repr_path.append(json_obj.get('name'))
                json_obj = json_obj.get(key)
        return repr_path

    def path_to_string(path):
        return json.dumps(path)
    
    def repr_path_to_string(path):
        repr_str = ''.join(path) 
        return repr_str

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