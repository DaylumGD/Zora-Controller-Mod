import json
import tkinter

def json_write(file, key, value, create=True):
    keys = []; values = []
    for k in json.load(open(file)):
        keys.insert(len(keys)+1, k)
        values.insert(len(keys)+1, json.load(open(file)).get(k))
    print(keys)
    print(values)

json_write('settings.json', False, False)