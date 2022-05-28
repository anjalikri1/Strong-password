digit=int(input("enter the digit: "))
alpha=input("enter the alphabet :")
spl=input("enter the special charector :")
if digit>=0:
    print("Digit =",digit)
    if alpha>="A" and alpha<="Z" or alpha>="a" and alpha<="z":
        print("Alphabet=",alpha)
        if spl=="#" or spl=="*" or spl=="@" or spl=="#" or spl=="$" :
            print("Special charector is :",spl)
            password=str(digit)+alpha+spl
            if len(password)>=8:
                print("This is strong password :",password)
            else:
                print("your password is too weak,password length should be 8 or more")
        else:
            print("Please enter the special charector :")
    else:
        print("alphabet charector must be there in password")
else:
    print("digit must be there in  your password")