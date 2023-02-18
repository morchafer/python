def isAnagram(text1, text2):
    exampleText = ""
    if type(exampleText) != type(text1) or type(exampleText) != type(text2):
        print("Error: isAnagram() requiere dos cadenas como argumentos ('text1', 'text2').")
        return
    elif text1 == exampleText or text2 == exampleText:
        print("Error: las cadenas ingresadas no pueden estar vacías.")
        return
    elif text1.isspace() or text2.isspace():
        print("Error: las cadenas ingresadas no pueden contener solo espacios.")
        return
    for a in text1:
        if a.isdigit():
            print("Error: las cadenas ingresadas no pueden contener dígitos.")
            return
    for b in text2:
        if b.isdigit():
            print("Error: las cadenas ingresadas no pueden contener dígitos.")
            return
    text1_, text2_ = '', ''
    for t1 in text1:
        if t1.isspace():
            continue  # ignora los espacios
        text1_ += t1  # si el caracter actual no es un espacio, lo concatena a la cadena 'text1_'
    for t2 in text2:
        if t2.isspace():
            continue
        text2_ += t2
    # compara la longitud de ambas cadenas para determinar si pueden ser anagramas o no
    if len(text1_) != len(text2_):
        return False
    text1 = text1_.lower()
    text2 = text2_.lower()
    for t2 in text2:  # itera cada caracter de text2...
        if t2 not in text1:  # ...y comprueba que esté dentro de text1
            return False  # con un solo caracter que no se encuentre en text1, retornará False, puesto que no pueden ser anagramas
    # si el bucle for termina con éxito, retorna True, significa que todos los caracteres de text2 se encuentran en text1, por lo tanto son anagramas.
    return True
