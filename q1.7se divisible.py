# 1 se 1000 tak saare numbers print karne ka loop likho. Lekin
#  * Agar number 3 se divisible hai toh "nav" print karvao.

#     Agar number 7 se divisible hai toh "gurukul" print karvao.
#     Agar number 21 se divisible hai toh "navgurukul" print karvao.

# Edit on Github


i=1
while i<1000:
    if i%21==0 :
        print("navgurukul",i)
    elif i%7==0:
        print("gurukul",i)
    elif i%3==0:
        print("nav",i)
    else:
        print("noting",i)
    i=i+1

