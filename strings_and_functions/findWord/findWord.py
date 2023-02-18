def findWord(word, text):

    # Manejo de errores:

    if type('') != type(word) or type('') != type(text):
        print("Error: findWord() requiere dos cadenas como argumentos ('word', 'text').")
        return
    elif len(word) > len(text):
        print("Error: el argumento 'word' no puede tener más caracteres que el argumento 'text'.")
        return
    for a in word:
        if not a.isalpha():
            print("Error: el argumento 'word' solo puede contener letras.")
            return
    for b in text:
        if not b.isalpha():
            print("Error: el argumento 'text' solo puede contener letras.")
            return

    # Inicia la lógica de la función:

    word = word.lower()
    text = text.lower()
    indexList = []
    index = 0
    for w in word:
        index = text.find(w, index)
        indexList.append(index)
    if -1 in indexList:
        count = 0
        for k in word:
            if k in text:
                count += 1
                if count == len(word):
                    print("La palabra '" + word +
                          "' no se encuentra dentro del texto '" + text + "'.")
                    print("Es posible que las letras de '" + word +
                          "' se encuentren dentro de '" + text + "'")
                    print("pero no en el orden correcto para formar la palabra.")
                    return False
            else:
                return False
    return True
