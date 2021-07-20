# Socho aapke paas 2 lists hain. 
# Aapne aisa code likhna hain jisse ek nayi list banne jisme 
# inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. Socho aapki do list yeh hain:
 
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 

# Inn dono list se aapki nayi list yeh banni chaiye:
 
# new_list = [1, 23, 75, 98]
i=0
b=[]
while i<len(list2) :
    a=list2[i]
    if a in list1:
        b.append(a)
        b.sort()
    i=i+1
print(b)
    




