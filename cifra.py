def cifra_cesar(texto, deslocamento):
    resultado = ""
    
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra) + deslocamento
            
            if letra.isupper():
                if codigo > ord('Z'):
                    codigo -= 26
                elif codigo < ord('A'):
                    codigo += 26
            elif letra.islower():
                if codigo > ord('z'):
                    codigo -= 26
                elif codigo < ord('a'):
                    codigo += 26
            
            resultado += chr(codigo)
        else:
            resultado += letra
    
    return resultado
