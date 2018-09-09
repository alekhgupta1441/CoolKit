import json

try:
    from lib.abs_path import abs_path
except:
    from abs_path import abs_path


def create_file(fille):
    template = {
        "coolkit":{
            "contest":"None",
            "type":"contest",
            "site":"codeforces",
            "prob":"A",
            "user":"-",
            "pswd":'-'
        }
    }
    jfile = open(fille, 'w')
    json.dump(template,jfile,indent = 4,ensure_ascii = False)
    jfile.close()


def extract_data(file_name):
    """
    Extracts json data from the given file
    if there is no such file
        it will create one
    if there is currupt file
        it will create new
    if file is ok
        it will return its content
    """
    fille = abs_path(file_name)
    try:
        jfile = open(fille)
    except FileNotFoundError:
        create_file(fille)
    jfile = open(fille)
    data = json.load(jfile)
    if(not 'coolkit' in data.keys()):
        create_file(fille)
        jfile = open(fille)
        data = json.load(jfile)
    return data['coolkit']


def _write_data(data,file_name):
    """
    Write RAW data into a json file
    """
    fille = abs_path(file_name)
    jfile = open(fille, 'w')
    data = {'coolkit':data}
    json.dump(data,jfile,indent = 4,ensure_ascii = False)
    jfile.close()


def dump_data(data,file_name):
    """
    create RAW data from LIST
    uses _write_data
    """
    fille = abs_path(file_name)
    dictt = extract_data(fille)
    for key in data:
        dictt[key] = data[key]
    _write_data(dictt,file_name)
