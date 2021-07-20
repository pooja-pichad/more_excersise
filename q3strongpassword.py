alphbate=input("enter a alphabte")
if alphbate>"A" or alphbate<"z" or alphbate>"a" or alphbate<"z":
    print(alphbate)
    s_charater=input("enter a character")
    if s_charater=="@" or s_charater=="#" or s_charater=="$":
        print(s_charater)
        number=int(input("enter a number"))
        if number>0:
            print(alphbate+s_charater+str(number))
            if  len(alphbate+s_charater+str(number))>8:
                print("strong password")
            else:
                print("its weak password")
        else:
            print("wrong number")
    else:
        print("wrong charcter try again")
else:
    print("wrong alphbate")
        