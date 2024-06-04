def decorator(funkcja):
    def wrapper(*args):
        if len(args) > 2:
            lista = []
            for arg in args:
                if isinstance(arg, int) or isinstance(arg, float):
                    lista.append(arg*arg)
                else:
                    raise TypeError('Numbers must be integers or floats')
            return lista
        else:
            return funkcja(*args)
    return wrapper
@decorator
def funkcja(*args):
    if len(args) == 1 and isinstance(args[0], list):
        iloczyn = 1
        for arg in args[0]:
            if isinstance(arg, int) or isinstance(arg, float):
                iloczyn *= arg
                continue
            else:
                raise TypeError("Argument must be a list or integer")
        return iloczyn

    elif len(args) > 2:
        suma = 0
        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                suma += arg
            else:
                raise TypeError("Argument must be integer")
        return suma
    else:
        print("Error")

from math import sqrt
def funkcja2(lista):
    """
    This function takes a list of numbers and returns a list of their sqrt using lambda and map

    Args:
        lista (list) - values

    Return:
         lista(list) - list of sqrt if everything goes well
         False - if something goes wrong
    """
    try:
        pierwiastki = list(map(lambda x: sqrt(x), lista))
    except NameError as e:
        print("Error", e)
        return False
    except ValueError as e:
        print(e)
        return False
    except TypeError as e:
        print(e)
        return False

    return pierwiastki

print(funkcja(1,2,3,4,5,6,7,8,9))
# print(funkcja2([1, 4, 9, 25]))

