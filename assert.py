def primera_letra(lista_palabras):
    primeras_letras = []

    for palabra in lista_palabras:
        assert type(palabra) == str, f'{palabra} no es una cadena de texto'
        assert len(palabra)>0, 'No se permiten elementos vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras
