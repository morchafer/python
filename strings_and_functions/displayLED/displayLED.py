nums = {
    '11': " # ", '12': " # ", '13': " # ", '14': " # ", '15': " # ",
    '21': "### ", '22': "  # ", '23': "### ", '24': "#   ", '25': "### ",
    '31': "### ", '32': "  # ", '33': "### ", '34': "  # ", '35': "### ",
    '41': "# # ", '42': "# # ", '43': "### ", '44': "  # ", '45': "  # ",
    '51': "### ", '52': "#   ", '53': "### ", '54': "  # ", '55': "### ",
    '61': "### ", '62': "#   ", '63': "### ", '64': "# # ", '65': "### ",
    '71': "### ", '72': "  # ", '73': "  # ", '74': "  # ", '75': "  # ",
    '81': "### ", '82': "# # ", '83': "### ", '84': "# # ", '85': "### ",
    '91': "### ", '92': "# # ", '93': "### ", '94': "  # ", '95': "### ",
    '01': "### ", '02': "# # ", '03': "# # ", '04': "# # ", '05': "### ",
}


def displayLED(n):
    example = 0
    if type(n) != type(example):
        print("Error: displayLED() solo acepta un valor entero como argumento.")
        return
    elif n < 0:
        print("Error: displayLED() espera un valor entero positivo.")
        return
    else:
        count = "1"
        arg = str(n) + " "
        while True:
            for i in arg:
                if count == "6":
                    return
                else:
                    if i != " ":
                        key = i + count
                        print(nums[key], end="")
                    else:
                        print()
                        count = int(count) + 1
                        count = str(count)
                        break
