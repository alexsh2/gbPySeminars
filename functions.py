def validateNumInput(msg1, msg2, msg5='', n=0):
    while True:
        try:
            num = int(input(msg1))
        except ValueError:
            print(msg2)
        else:
            if (n != 0 and len(str(num)) == n) or n == 0:
                return num
            else:
                print(msg5)
