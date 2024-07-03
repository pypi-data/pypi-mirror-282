import json
import re
def formatter22(ok):
 def eliminar_cadena_generic(te):
    pattern = r'",null,null,null,"generic".*'
    te = re.sub(pattern, '', te)
    return te
 def eliminar_cadena_generic2(te):
    pattern = r']],true,null,null,[],[".*'
    te = re.sub(pattern, '', te)
    return te

 with open("datos.json", "r") as file:
    te = file.read()

 te = te.replace('\\"', '"')
 te = te.replace('\\\\\\\\"', "'")
 te = te.replace('"[[', "[[")
 te = te.replace('activado"]]"', 'activado"]]]]]]]]')

 te = eliminar_cadena_generic(te)
 te = eliminar_cadena_generic2(te)

 with open("datos.json", "w") as file:
     file.write(te)

 try:
     json_data = json.loads(te)
 except json.JSONDecodeError as e:
     print(f"Error al decodificar JSON: {e}")
