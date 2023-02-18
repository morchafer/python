import mysql.connector


def login():
    try:
        global cursor, cnx
        print("\n\t\t-----Formulario de logueo a MySql-----")
        user_ = input("Ingresa el usuario: ")
        password_ = input("Ingresa la contraseña: ")
        host_ = input("Ingresa el host: ")
        database_ = input("Ingresa el nombre de la base de datos: ")
        cnx = mysql.connector.connect(
            user=user_, password=password_, host=host_, database=database_, auth_plugin='mysql_native_password')
        cursor = cnx.cursor()
        table_()
    except KeyboardInterrupt:
        print("\n\nSe interrumpió la sesión.")
    except:
        print("\nError: los datos ingresados son incorrectos.")
        print("       Inténtalo de nuevo.")
        login()


def table_():
    global select, tableG
    try:
        table = input("Ingresa el nombre de la tabla: ")
        tableG = table
        select = "select * from " + table
        cursor.execute(select)
        print("\n...")
        print("\nContenido actual de la tabla", table + ":\n")
        for idb, name, category, price in cursor:
            print(idb, name, category, price)
        form()
    except KeyboardInterrupt:
        print("\n\nSe interrumpió la sesión.")
    except:
        print("\nError: es posible que el nombre de la tabla sea incorrecto")
        print("        o no haya sido creada todavía. Inténtalo de nuevo.")
        table_()


def form():
    try:
        global idBook, insert
        print("\n\t\t----------Formulario de registro----------")
        idBook = int(input("Ingresa el ID del libro: "))
        nameBook = input("Ingresa el nombre del libro: ")
        catBook = input("Ingresa la categoría del libro: ")
        priceBook = int(input("Ingresa el precio del libro: "))
        insert = "insert into " + tableG + \
            " values (" + str(idBook) + ", '" + nameBook + \
            "', '" + catBook + "'," + str(priceBook) + ")"
        rollbackEval()
    except KeyboardInterrupt:
        print("\n\nSe interrumpió la sesión.")
    except ValueError:
        print("\nError: ingresa un valor entero.")
        form()


def rollbackEval():
    count = 0
    cursor.execute("begin")
    cursor.execute(insert)
    cursor.execute(select)
    print("\n...")

    for idb, name, category, price in cursor:
        if idb == idBook:
            count += 1
    if count >= 2:
        cnx.rollback()
        print("\nError: un libro con el mismo ID ya se encuentra registrado en la tabla.\n")
        cursor.execute(select)
        for idb, name, category, price in cursor:
            print(idb, name, category, price)
        try:
            choice = input("¿Quieres registrar otro libro? (y/n): ")
            while choice != "y" and choice != "n":
                choice = input("Error: ingresa una respuesta correcta (y/n): ")
            if choice == "y":
                cnx.commit()
                form()
            elif choice == "n":
                print("\nConexión finalizada.")
                cnx.commit()
                cursor.close()
                cnx.close()
        except KeyboardInterrupt:
            cnx.commit()
            print("\n\nSe interrumpió la sesión.")

    else:
        print("\nLibro registrado exitosamente.\n")
        cursor.execute(select)
        for idb, name, category, price in cursor:
            print(idb, name, category, price)
        try:
            choice = input("¿Quieres registrar otro libro? (y/n): ")
            while choice != "y" and choice != "n":
                choice = input("Error: ingresa una respuesta correcta (y/n): ")
            if choice == "y":
                cnx.commit()
                form()
            elif choice == "n":
                print("\nConexión finalizada.")
                cnx.commit()
                cursor.close()
                cnx.close()
        except KeyboardInterrupt:
            cnx.commit()
            cursor.close()
            cnx.close()
            print("\n\nSe interrumpió la sesión.")


login()
