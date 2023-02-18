def cipherC(message, steps):
    exampleMessage = ""
    exampleSteps = 0
    if type(message) != type(exampleMessage):
        print("Error: 'message' requiere una cadena como argumento.")
        return
    elif type(steps) != type(exampleSteps):
        print("Error: 'steps' requiere un valor entero como argumento.")
        return
    elif steps <= 0:
        print("Error: 'steps' requiere un valor entero positivo como argumento.")
        return
    elif steps > 25:
        print("Error: 'steps' debe estar en el rango de 1 a 25.")
        return
    cipher = ''
    for c in message:
        if not c.isalpha():
            cipher += c
            continue
        elif c.isupper():
            code = ord(c)
            for i in range(steps):
                if code == 90:
                    code = 65
                    continue
                code += 1
            cipher += chr(code)
        elif c.islower():
            code = ord(c)
            for i in range(steps):  # (97-122)
                if code == 122:
                    code = 97
                    continue
                code += 1
            cipher += chr(code)
    return cipher
