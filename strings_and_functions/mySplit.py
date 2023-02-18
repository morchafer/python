def mySplit(strng):
    strngList = []
    strng_ = ""
    if type(strng) == type(strng_):
        if strng == strng_:
            return strngList
        elif " " not in strng:
            strngList.append(strng)
            return strngList
        else:
            for i in strng:
                if i != " ":
                    strng_ += i
                elif i == " ":
                    if strng_ != "":
                        strngList.append(strng_)
                    strng_ = ""  # reiniciando strng_
            if strng[-1] != " ":
                strngList.append(strng_)
            return strngList
    else:
        print("Error: mySplit() solo acepta una cadena como argumento.")
        return
