def divide_elementos(lista_, divisor_):
    try:
        return [i / divisor_ for i in lista_]
    except ZeroDivisionError as error:
        print(error)
        return lista_

lista = list(range(10))
divisor = 0

print(divide_elementos(lista, divisor))
