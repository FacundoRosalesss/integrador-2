def es_int(
    cadena: str
    ) -> bool:
    """
    verifica que cadena sea un integer
    """

    if not cadena:
        return False

    for i in range(len(cadena)):
        if cadena[i] < "0" or cadena[i] > "9":
            return False

    return True