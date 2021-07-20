# Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul ka ek 
# mahine ka kharcha nikalenge input ka use kar ke do values ka input lo: * Number of students

#     Ek student ka kharcha

# Iss ke hisaab se total kharcha nikalein. Agar total kharcha 50000 (50 hazar) ya usse kam hai toh print
#  karein "Hum budget ke andar hain" nahi toh print karo ki hum budget ke bahar hain. 
# Note: Inn exercises mein aapko variables ke naam apne aap soch kar likh
number_of_student=int(input("enter a number"))
student_ka_kharcha=int(input("enter a khracha"))
if student_ka_kharcha<50000:
    print("buget mai hai")
else:
    print("buget mai nhi hai")

