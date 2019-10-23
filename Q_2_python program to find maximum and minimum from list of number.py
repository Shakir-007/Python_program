#Name = Mohd_Shakir
#Roll_No = 08
#Enrollment_No = A180478


lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst))
print( "Minimum element in the list is :", min(lst))
