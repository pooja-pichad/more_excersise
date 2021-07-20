# Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke elements
#  hone chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek 
#  baar hi hone chaiye. Agar humare paas yeh do lists hain:
 
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 

# Toh humari nayi list yeh hogi:
#  
# new_list = [1, 2, 5, 10, 12, 13, 16, 20] 

# Yahan dekho ki dono lists ke items ek ek baar aa rahe hain. * Jaise dono lists mein 
# 1 aa raha tha, lekin nayi list mein ek hi baar aa raha hai.

    # Aise hi 10 aur 16 bhi dono list mein aa raha tha, lekin nayi list mein ek hi baar hai
    # Aur 5, 2, 12, 13 aur 20 mein se kuch pehli list mein the aur kuch dusri mein, lekin

i=0
a=[]
while i<len(list1):
    b=list1[i]
    if b  not in list2:
        a.append(b)
    i=i+1
    j=0
while j<len(list2):
    c=list2[j]
    a.append(c)
    j=j+1
print(a)
# i=i+1

