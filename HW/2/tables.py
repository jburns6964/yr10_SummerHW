Z = True
b = True

while b == True:
    P = int(input("which times table would you like to see? "))
    U = int(input("what number would you like it to go up to? "))
    B = 0
    while B != U+1:
        print("{0}x{1}={2}".format(P,B,P*B))
        B = B+1
    F = input("would you like to stop?(y/n) ")
    while Z == True:
        if F == "y" or F == "Y":
            b = False
            Z = False
        elif F == "n" or F == "N":
            Z = False
            pass
        else:
            print("Try again")
