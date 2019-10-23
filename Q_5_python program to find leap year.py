#Name = Mohd_Shakir
#Roll_No = 08
#Enrollment_No = A180478



year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
      print("{0} is a leap year".format(year))  
else:  
           print("{0} is not a leap year".format(year))  
