import requests
import json

ROUTE_BASE = "https://octopus.heuritech.com/thesaurus/"


# helper functions
def get_entities_from_json(js):
    if "entities" in js:
        return [ent["id"] for ent in js["entities"]]
    else:
        return []


# Routes wrappers
def get_name(idname):
    res = requests.get(ROUTE_BASE + "get_name_from_id?id=" + idname)
    return res.json()


def get_entity(name, nomenclature_id=None):
    request = ROUTE_BASE + "get_id_from_name?name=" + name
    if nomenclature_id:
        request = request + "?nomenclature_id=" + nomenclature_id
    res = requests.get(request)
    js = res.json()
    ents = get_entities_from_json(js)
    if len(ents) != 1:
        print("warning len(ent) = "+str(len(ents)))
        return None
    else:
        return ents[0]


def get_children_entities(entity):
    res = requests.post(ROUTE_BASE + "list_entities",
                        data=json.dumps({"parent": entity}),
                        headers={'Content-type': 'application/json', 'Accept': 'application/json'})
    js = res.json()
    return get_entities_from_json(js)


def update_image(entity, md5, action="add"):
    dic = {"entity_id": entity, "images": [{"image_md5": md5, "type": "positive", "action": action}]}
    res = requests.post(ROUTE_BASE + "update_images",
                        data=json.dumps(dic),
                        headers={'Content-type': 'application/json', 'Accept': 'application/json'})
    return res.status_code


def get_entity_details(entity, nomenclature_id=None):
    dic = {"id": entity}
    if nomenclature_id:
        dic["nomenclature_id"] = nomenclature_id
    res = requests.post("https://octopus.heuritech.com/thesaurus/list_entities",
                        data=json.dumps(dic),
                        headers={'Content-type': 'application/json', 'Accept': 'application/json'})
    js = res.json()
    return js
