import json
import sys

_nombre = "".join(sys.argv[1:]) if len(sys.argv) > 1 else 'Luis'

with open('mensajes.json', 'r', encoding='utf8') as _f:
    _Datos = json.load(_f)
    for _k, _i in _Datos.items():
        _Datos[_k] = _i.replace('###', _nombre)

while True:
    print(_Datos['pregunta'], _Datos['acciones'])
    _r = int(input())

    if _r == 1:
        break

    print(_Datos['no'])
    
print(_Datos['si'])