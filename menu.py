from inputs import pedir_int
from funcionalidades import crear_alumno, listar_alumno, buscar_alumno, modificar_alumno, eliminar_alumno, estadisticas

def menu():
    """
    Muestra el menú principal y retorna la opción seleccionada.
    
    arg:
        None
    
    returns:
        opcion: int
        None
    """
    print("\n========= GESTIÓN DE ALUMNOS =========")
    print("1. Cargar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumnos")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Estadisticas")
    print("7. Salir")
    
    opcion = pedir_int("\nIngrese una opcion: \n", 1, 7)
    
    match opcion:
        case 1:
            crear_alumno()
        case 2:
            listar_alumno()
        case 3:
            buscar_alumno()
        case 4:
            modificar_alumno()
        case 5:
            eliminar_alumno()
        case 6:
            estadisticas()
        case 7:
            print("Saliendo...")
            return opcion


    
    
