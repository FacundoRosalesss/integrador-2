import json

ALUMNOS = "data/alumnos.json"

def cargar_alumnos():
    """
    funcion para cargar la informacion del archivo json
    
    arg:
        None
    
    returns:
        archivo: list
    """
    with open(ALUMNOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
    
def guardar_alumnos(
    alumnos:list
    ) -> None:
    """
    funcion para guardar la informacion en el archivo json
    
    arg:
        alumnos: list
    
    return:
        None
    """
    with open(ALUMNOS, "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)
        

        
