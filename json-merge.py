import json


def get_file(file_path):
    with open(file_path, "r+") as f:
        a = f.read()
        return a


def write_file():
    with open('./zh.json', "r+") as f:
        f.write(str(source_json))
        f.close()


source_json = get_file('./zh.source.json')


temp = json.dumps(source_json, encoding="utf-8")
print('dumps------', temp)

temp = json.loads(source_json, encoding="utf-8")
print('loads------', temp)
