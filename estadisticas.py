from archivos import cargar_alumnos

def cantidad_alumnos():
    """
    Retorna la cantidad de alumnos registrados.
    
    Args:
        None
    
    Returns:
        None
    """
    alumnos = cargar_alumnos()
    print(f"La cantidad de alumnos es: {len(alumnos)}")
    

def promedio_notas():
    """
    Retorna el promedio de notas de los alumnos registrados.
    
    Args:
        None
    
    Returns:
        None
    """
    alumnos = cargar_alumnos()
    acumulador_nota = 0
    for alumno in alumnos.values():
        acumulador_nota += alumno["nota_final"]
    print(f"El promedio de notas de los alumnos es: {acumulador_nota / len(alumnos):.1f}")
    

def mayor_nota():
    """
    Retorna la mayor nota de los alumnos registrados con sus nombres.
    
    Args:
        None
    
    Returns:
        None
    """
    alumnos = cargar_alumnos()
    mayor_nota = 0
    alumno_mayor_nota = ""
    for alumno in alumnos.values():
        if alumno["nota_final"] > mayor_nota:
            mayor_nota = alumno["nota_final"]
            alumno_mayor_nota = f"{alumno['nombre']} {alumno['apellido']}"
    print(f"La mayor nota es {mayor_nota} de {alumno_mayor_nota}")
    

def cantidad_aprobados():
    """
    Retorna la cantidad de alumnos aprobados.
    
    Args:
        None
    
    Returns:
        None
    """
    alumnos = cargar_alumnos()
    aprobados = 0
    for alumno in alumnos.values():
        if alumno["nota_final"] >= 6:
            aprobados += 1
    print(f"La cantidad de alumnos aprobados es: {aprobados}")
    
    
def cantidad_desaprobados():
    """
    Retorna la cantidad de alumnos desaprobados.
    
    Args:
        None
    
    Returns:
        None
    """
    alumnos = cargar_alumnos()
    desaprobados = 0
    for alumno in alumnos.values():
        if alumno["nota_final"] < 6:
            desaprobados += 1
    print(f"La cantidad de alumnos desaprobados es: {desaprobados}")


