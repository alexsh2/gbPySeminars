def validateNumInput(str1, str2, str3='', n=0):
    while True:
        try:
            num = int(input(str1))
        except ValueError:
            print(str2)
        else:
            if (n != 0 and len(str(num)) == n) or n == 0:
                return num
            else:
                print(str3)


def validateYesNo():
    while True:
        decision = input()
        if decision.lower() == "да":
            return True
        elif decision.lower() == "нет":
            return False
        else:
            print("Введите \"да\", или \"нет\": ")
