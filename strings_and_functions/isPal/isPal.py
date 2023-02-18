def isPal(text):
    exampleText = ""
    if type(text) != type(exampleText):
        print("Error: isPal() requiere una cadena como argumento.")
        return
    elif text == exampleText:
        print("La cadena ingresada está vacía.")
        return
    elif text.isspace():
        print("La cadena ingresada no contiene letras.")
        return
    for d in text:
        if d.isdigit():
            print("La cadena ingresada no puede contener dígitos.")
            return
    count = -1
    textFront = ''
    textBack = ''
    for c in text:
        if c.isspace():
            continue
        else:
            textFront += c
    for i in range(len(text)):
        if text[count].isspace():
            count -= 1
            continue
        else:
            textBack += text[count]
            count -= 1
    textFront_ = textFront.lower()
    textBack_ = textBack.lower()
    count_ = 0
    for j in textFront_:
        if j == textBack_[count_]:
            count_ += 1
            continue
        else:
            return False
    return True
