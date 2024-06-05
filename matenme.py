import json


with open('mensajes.json', 'r', encoding='utf8') as _f:
    _Datos = json.load(_f)

# while True:
    print(_Datos['pregunta'])
    _r = input()
    