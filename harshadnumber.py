

x = 42
x_digits = list(str(x)) 
#print(x_digits)
i=0
t=[]
while i<len(x_digits):
    a=int(x_digits[i])
    t.append(a)
    i=i+1
#print(t)
j=0
sum=0
while j<len(t):
    sum=sum+t[j]
    j=j+1
#print(sum)
x=42
if x%sum==0:
    print("true")
else:
    print("false")
