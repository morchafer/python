from os import strerror


def chistogram(file_name):

    # Manejo de errores con condicionales:

    if type(file_name) != type(''):
        print('Error: Se debe ingresar una cadena para el nombre del archivo.')
        quit()
    if '.txt' in file_name:
        print('Error: No es necesario especificar la extensión ".txt".')
        quit()

    # Inicia el bloque try-except:

    try:
        fileR = open(file_name + '.txt', 'rt', encoding='utf-8')
        letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
                   'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
                   'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                   'y': 0, 'z': 0}
        for ch in fileR.read():
            for l in letters:
                if ch.lower() == l:
                    letters[l] += 1
        noZeroDict = {}
        for l in letters:
            if letters[l] == 0:
                continue
            noZeroDict[l] = letters[l]
        val = list(noZeroDict.values())
        control = True
        def sortV(a, b): return a < b
        while control:
            control = False
            for i in range(len(val) - 1):
                if sortV(val[i], val[i+1]):
                    control = True
                    val[i], val[i+1] = val[i+1], val[i]
        key = list(noZeroDict.keys())
        sortList = []
        for v in val:
            for k in range(len(key)):
                if v == noZeroDict[key[k]]:
                    sortList.append(key[k])
                    del key[k]
                    break
        fileR.close()
        fileW = open(file_name + '.hist', 'wt', encoding='utf-8')
        count = 0
        for d in sortList:
            fileW.write(d + ' -> ' + str(val[count]) + '\n')
            print(d + ' -> ' + str(val[count]))
            count += 1
        fileW.close()
    except Exception as e:
        print('Error:', strerror(e.errno))
