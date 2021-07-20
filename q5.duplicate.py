string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
i=0
a=[]
while i<len(string_list):
    b=string_list[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)

