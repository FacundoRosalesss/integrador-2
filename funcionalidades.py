from archivos import cargar_alumnos, guardar_alumnos
from inputs import pedir_string, pedir_int

def crear_alumno():
    """
    Crea un nuevo alumno y lo guarda en el archivo json.
    
    Args:
        None
    
    Returns:
        None
    """
    alumno = cargar_alumnos()
    
    id_alumno = pedir_string("Ingrese el ID del alumno: ")
    if id_alumno in alumno:
        print("El ID ya existe")
        return
    
    dni = pedir_int("Ingrese el DNI del alumno: ", 1000000, 99999999)
    nombre = pedir_string("Ingrese el nombre del alumno: ")
    apellido = pedir_string("Ingrese el apellido del alumno: ")
    edad = pedir_int("Ingrese la edad del alumno: ", 1, 120)
    nota_final = pedir_int("Ingrese la nota final del alumno: ", 0, 10)
    
    alumno[id_alumno] = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota_final": nota_final
    }
    
    guardar_alumnos(alumno)
    print("Usuario creado correctamente")
    

def listar_alumno():
    """
    Lista todos los alumnos registrados.
    
    Args:
        None
    
    Returns:
        None
    """
    alumno = cargar_alumnos()
    for id_alumno, alumno in alumno.items():
        print("------------------------")
        print(f"ID: {id_alumno}")
        print(f"DNI: {alumno['dni']}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Nota final: {alumno['nota_final']}")
        print("------------------------")
    

def buscar_alumno():
    """
    Busca un alumno por su DNI.
    
    Args:
        None
    
    Returns:
        None
    """
    alumno = cargar_alumnos()
    
    dni_alumno = pedir_string("Ingrese el DNI del alumno a buscar: ")
    
    for id_alumno, datos in alumno.items():
        if str(datos["dni"]) == dni_alumno:
            print("------------------------")
            print(f"ID: {id_alumno}")
            print(f"DNI: {datos['dni']}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Apellido: {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Nota final: {datos['nota_final']}")
            print("------------------------")
            return
    
    else:
        print("El DNI no existe")  
    

def modificar_alumno():
    alumno = cargar_alumnos()
    
    codigo = pedir_string("\nIngrese el ID del alumno a modificar: ")
    
    if codigo not in alumno:
        print("\nEl ID de alumno no existe")        
        return
    
    dni = pedir_int("Ingrese el nuevo DNI del alumno: ", 10000000, 999999999)
    nombre = pedir_string("Ingrese el nuevo nombre del alumno: ")
    apellido = pedir_string("Ingrese el nuevo apellido del alumno: ")
    edad = pedir_int("Ingrese la nueva edad del alumno: ", 1, 120)
    nota_final = pedir_int("Ingrese la nueva nota final del alumno: ", 0, 10)
    
    alumno[codigo]["dni"] = dni
    alumno[codigo]["nombre"] = nombre
    alumno[codigo]["apellido"] = apellido
    alumno[codigo]["edad"] = edad
    alumno[codigo]["nota_final"] = nota_final
    
    guardar_alumnos(alumno)
    print("\nUsuario modificado correctamente")
    
    
    


def eliminar_alumno():
    """
    Elimina un alumno por su DNI.
    
    Args:
        None
    
    Returns:
        None
    """
    alumno = cargar_alumnos()
    
    dni_alumno = pedir_string("\nIngrese el DNI del alumno a eliminar: ")
    
    for id_alumno, datos in alumno.items():
        if str(datos["dni"]) == dni_alumno:
            del alumno[id_alumno]
            guardar_alumnos(alumno)
            print("\nUsuario eliminado correctamente")
            return
    
    print("\nEl DNI no existe")

def estadisticas():
    """
    Muestra las estadísticas de los alumnos.
    
    Args:
        None
    
    Returns:
        None
    """
    import estadisticas
    estadisticas.cantidad_alumnos()
    estadisticas.promedio_notas()
    estadisticas.mayor_nota()
    estadisticas.cantidad_aprobados()
    estadisticas.cantidad_desaprobados()