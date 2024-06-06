import json


with open('mensajes.json', 'r', encoding='utf8') as _f:
    _Datos = json.load(_f)

while True:
    print(_Datos['pregunta'], _Datos['acciones'])
    _r = int(input())

    if _r == 1:
        break

    print(_Datos['no'])
    
print(_Datos['si'])