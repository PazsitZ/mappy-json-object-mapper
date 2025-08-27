import json
from types import SimpleNamespace


def is_primitive(param):
    primitive = (type (int), type (str), type (bool))
    return type (param) in primitive

def transformToSimpleNamespace(jsonStr):
    jsonObj = json.loads(jsonStr, object_hook=lambda d: SimpleNamespace(**d))
    return jsonObj

def get_setters(clazz=None):
    for attribute in clazz.__dict__.keys():
        if attribute[:2] != '__':
            value = getattr(clazz, attribute)
            if not callable(value):
                print(attribute, '=', value)