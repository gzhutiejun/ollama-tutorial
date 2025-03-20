import json


def serialize_json_object(jsonObj: dict):
    return json.dumps(jsonObj, allow_nan= True)

data: dict = {
    'currency':'',
    'value':0
}
print(serialize_json_object(data))