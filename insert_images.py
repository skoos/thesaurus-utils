import json
from thesaurus_wrapper import insert_image
import os

#
# Untested 
#

# insert folder of images in cacher
def cache_images(path_in, path_out, passwd):
    cmd = "docker run -it -v " + \
          path_in + \
          ":/img:ro --entrypoint python3 docker.heuritech.com/pipeline-insertor:2017051617 Insertor.py -p " + \
          passwd + \
          " -img /img --to-labelling" + \
          " > path_out"

    print(cmd)
    os.sys(cmd)

# build the name to entity dictionary from the folder
def build_list_of_folders(path):
    folders = sorted(os.listdir(path))
    name_to_ent = {x:get_entity(x) for x in folders}
    return name_to_ent

# Read a json output of a cacher
def read_and_insert(json_file, name_to_ent):
    h = open(json_file)

    for line in h:
        l = json.loads(line)
        md5 = l["image_md5"]
        path = l["image_path"]
        name = path.split("/")[2]
        ent = name_to_ent[name]
        res = update_image(ent, md5)
        print("Sending: ", ent, md5, "response: ", res)

# Execute whole script
def insert_images(path, passwd):
    temp_json_file = path + "list.json"
    
    cache_images(path, temp_json_file, passwd)

    name_to_ent = build_list_of_folders(path)

    read_and_insert(temp_json_file, name_to_ent)

    print("successfully inserted images")
