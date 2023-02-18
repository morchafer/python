from os import strerror

# Excepción general de la función; maneja el error provocado por la inexistencia del archivo.


class StudentEvaluationError(Exception):
    def __init__(self):
        self.error = 'StudentEvaluationError: imposible terminar la ejecución; el archivo no ha sido encontrado en el directorio: '

# Excepción para el manejamiento de errores relacionados con el vacío del archivo.


class EmptyFileError(StudentEvaluationError):
    def __init__(self):
        self.error = 'EmptyFileError: el archivo está vacío: '

# Excepción para el manejamiento de errores relacionados con problemas de sintaxis en las líneas del archivo.


class LineError(StudentEvaluationError):
    def __init__(self):
        self.error = 'LineError: una línea del archivo no es apta para el procesamiento de los datos: '

# Clase de ayuda cuyo propósito es brindar información general sobre el funcionamiento de studentEval().


class HelpClass(StudentEvaluationError):
    def __init__(self):
        self.consejo = 'Consejo: este es el formato en el que se deben presentar los datos por cada línea del archivo de texto: '
        self.formato = 'Formato: [nombre_estudiante][espacio][apellido_estudiante][espacio][puntos_del_estudiante]'
        self.ejemplo = 'Ejemplo: Daniel Chavarin 10'
        self.nota = 'Nota: los puntos del estudiante pueden ser enteros o decimales; en caso de decimales se recomienda colocar'
        self.nota_2 = 'un máximo de dos dígitos después del punto decimal; en caso de enteros se recomienda máximo cuatro dígitos.'
        self.ejemplo_2 = 'Ejemplos con punto decimal: Daniel Chavarin 9.5 / Daniel Chavarin 0.5 / Daniel Chavarin 9.56'
        self.nota_3 = 'Nota 2: el nombre y el apellido del estudiante solo pueden contener letras del alfabeto latino. En caso de'
        self.nota_4 = 'necesitar abreviar el nombre o apellido, se recomienda hacerlo sin el punto final de cada abreviación, de lo'
        self.nota_5 = 'contrario se producirá un error.'
        self.ejemplo_3 = 'Ejemplo con abreviación: Dan Chav 10'

# Excepción cuyo propósito es el manejo del error provocado por el mal ingreso del nombre del archivo como argumento.


class FileNameError(StudentEvaluationError):
    def __init__(self):
        self.error = 'FileNameError: la función studentEval() requiere una cadena (\'file_name\') como argumento.'

# Excepción cuyo propósito es el manejo del error provocado por el exceso de dígitos enteros en el puntaje del estudiante.


class IntCounterError(StudentEvaluationError):
    def __init__(self):
        self.error = 'IntCounterError: el puntaje del estudiante excedió el límite de dígitos enteros (4): '


def studentEval(file_name):
    try:
        if type(file_name) != type(''):  # Manejo de errores para la excepción FileNameError
            raise FileNameError
        elif file_name == 'help':  # Acceso al comando 'help' de la función
            print('\n\tLa palabra reservada \'help\' arrojará información acerca del uso correcto de la función studentEval().')
            print('\n\tNota: \'help\' es una palabra reservada para la función studentEval(), por lo tanto no puede usarse')
            print('\tcomo argumento de nombre de archivo.')
            raise HelpClass
        elif '.txt' in file_name:  # Asegura el ingreso correcto del nombre del archivo a ser procesado en la función
            print('\n\tNo es necesario especificar la extensión \'.txt\' en el nombre del archivo. La función studentEval() lo hace automáticamente.')
            raise StudentEvaluationError

        file = open(file_name + '.txt', 'rt', encoding='utf-8')
        fileR = file.readlines()
        file.close()

        # Inicia el manejo de errores para la excepción EmptyFileError:

        if fileR == []:
            raise EmptyFileError
        for_control = False
        for line in range(len(fileR)):
            for byte in fileR[line]:
                if byte.isspace() or byte == '\t' or byte == '\n':
                    continue
                for_control = True
                break
            if for_control:
                break
            elif line == len(fileR)-1:
                raise EmptyFileError

        students = {}
        line_number = 0
        name = ''
        lastname = ''
        full_name = ''
        score = ''
        score_2 = ''
        name_control = True
        lastname_control = True
        dot_control = False
        float_control = False
        int_counter = 0
        spaces_counter = 0

        for n in range(len(fileR)):
            if fileR[n].endswith('\n'):
                continue
            fileR[n] += '\n'
        for line in fileR:
            line_number += 1
            line_2 = line.replace('\t', ' ')
            for spcs in line_2:
                if spcs == ' ':
                    spaces_counter += 1
            if spaces_counter != 2:
                raise LineError
            else:
                for ch in range(len(line_2)):
                    if line_2[ch].isspace():
                        if name_control:
                            name = line_2[:ch]
                            if len(name) != 0:
                                for n in name:
                                    if n.isalpha():
                                        continue
                                    raise LineError
                            else:
                                raise LineError
                            name += ' '
                            name_control = False
                        elif lastname_control:
                            lastname = line_2[len(name):ch]
                            if len(lastname) != 0:
                                for ln in lastname:
                                    if ln.isalpha():
                                        continue
                                    raise LineError
                            else:
                                raise LineError
                            lastname += ' '
                            full_name = name + lastname
                            lastname_control = False

                for ch in range(len(line_2)):
                    if line_2[ch] == '\n':
                        score = line_2[len(full_name):ch]
                        if len(score) != 0:
                            for sc in range(len(score)):
                                if score[sc].isdigit():
                                    continue
                                elif score[sc] == '.' and dot_control == False and sc != len(score)-1:
                                    dot_control = True
                                else:
                                    raise LineError
                            for sc in range(len(score)):
                                if score[sc] != '.' and float_control == False:
                                    int_counter += 1
                                    if int_counter > 4:
                                        raise IntCounterError
                                    score_2 += score[sc]
                                    continue
                                float_control = True
                                score_2 += score[sc]
                                if len(score_2) == int_counter+3:
                                    break
                        else:  # Este else es la respuesta al filtro que condiciona si 'score' está vacío...
                            # ...entonces, se levantaría la excepción LineError.
                            raise LineError

            if len(full_name) > 30:
                full_name = full_name[:30]
            if full_name in students:
                students[full_name] += float(score_2)
            else:
                students[full_name] = float(score_2)

            name = ''
            lastname = ''
            full_name = ''
            score = ''
            score_2 = ''
            name_control = True
            lastname_control = True
            dot_control = False
            float_control = False
            int_counter = 0
            spaces_counter = 0

        sKeys = list(students.keys())
        sKeys.sort()

        print('\n+======== PUNTAJE GENERAL DE CADA ESTUDIANTE ========+')
        for s in sKeys:
            spaces = 32 - len(s)
            print('|\t\t\t\t    |\t\t     |\n|   ' + s, end='')
            for sp in range(spaces):
                print(' ', end='')
            print('|    ', end='')
            spaces = 7 - len(str(students[s]))
            spaceString = ''
            for sp in range(spaces):
                spaceString += ' '
            spaceString += str(students[s])
            print(spaceString + '     |')
        print('|\t\t\t\t    |\t\t     |')
        print('+====================================================+\n')

    # Manejo de las excepciones:

    except HelpClass as HC:
        print('\n+================================================ H    E   L   P =================================================+')
        print('|                                                                                                                 |')
        print('|   ' + HC.consejo + '      |')
        print('|                                                                                                                 |')
        print('|   ' + HC.formato + '                    |')
        print('|                                                                                                                 |')
        print('|   ' + HC.ejemplo +
              '                                                                                   |')
        print('|                                                                                                                 |')
        print('|   ' + HC.nota + '    |' + '\n|   ' + HC.nota_2 + '   |')
        print('|                                                                                                                 |')
        print('|   ' + HC.ejemplo_2 + '                  |')
        print('|                                                                                                                 |')
        print('|   ' + HC.nota_3 + '    |' + '\n|   ' + HC.nota_4 + '  |')
        print('|   ' + HC.nota_5 +
              '                                                                              |')
        print('|                                                                                                                 |')
        print('|   ' + HC.ejemplo_3 +
              '                                                                          |')
        print('|                                                                                                                 |')
        print('+=================================================================================================================+\n')

    except IntCounterError as ICE:
        print('\n\t' + ICE.error + line_2)
        print('\tError en la línea número ' + str(line_number) + '.\n')

    except LineError as LE:
        print('\n\t' + LE.error + "'línea número: " + str(line_number) + "'")
        print('\n\tError en la línea número ' + str(line_number) +
              '. Contenido actual de la línea: ' + line_2)
        print('\tPara obtener ayuda sobre el funcionamiento de studentEval(), utiliza el comando \'help\': studentEval(\'help\').\n')

    except EmptyFileError as EFE:
        print('\n\t' + EFE.error + "'" + file_name + '.txt' + "'\n")

    except FileNameError as FNE:
        print('\n\t' + FNE.error)
        print('\n\tSe ha ingresado \'' + str(file_name) + '\' como argumento.\n')

    except StudentEvaluationError as SEE:
        print('\n\t' + SEE.error + "'" + file_name + '.txt' + "'\n")

    except FileNotFoundError as FNFE:
        try:
            raise StudentEvaluationError
        except StudentEvaluationError as SEE:
            print('\n\t' + SEE.error + "'" + file_name + '.txt' + "'\n")

    except Exception as E:
        print('\n\tSe produjo un error de E/S: ', strerror(E.errno) + '\n')
