from thesaurus_wrapper import *
import json

print("name for %%lu:01000061")
name = get_name('%%lu:01000061')
print(name)

print("entity for boy")
ent_name = get_entity("boy")
print(ent_name)

print("details for entity %%lu:01000061")
ent_details = get_entity_details('%%lu:01000061', "24")
print(ent_details)

print("add a fake md5 to entity")
entity = "%%lu:01000061"
md5 = 234252f232
result = insert_image(entity, md5, action="add")
print("result: ", result)
