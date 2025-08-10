from datetime import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")

def validate_positive_int(value_str):
    try:
        value = int(value_str)
        if value <= 0:
            raise ValueError("El valor debe ser positivo")
        return value
    except ValueError:
        raise ValueError("Debe ingresar un número entero válido")