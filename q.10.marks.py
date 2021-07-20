# Socho aapke paas ek school ki class mein har student ke har subject ke marks hain. Jaise
 
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 

# Yeh ek list mein andar aur lists hain. Andar waali list mein har bache ke saare subjects mein marks hain.
#  Ek max_marks naam ka function banao jo ki ek aisi list le aur har students ke maximum marks print kare. J
# aise agar main aapke max_marks function ko upar waali list ke saath call karunga ,
 
# max_marks(marks) 

# Toh uski output yeh honi chaiye: Dekhiye ki har line har student ke maximum marks print hue hain.
# Edit on Github

def max_marks(max):
    i=0
    while i<len(marks):
        a=marks[i]
        j=0
        while j<len(marks):
            b=marks[j]
            c=max(marks[i])
            j=j+1
        i=i+1
        print(c)
max_marks(max)