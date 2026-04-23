number = input("Enter a number: ")
m1= int("%s" % number)
m2= int("%s%s" % (number, number))
m3= int("%s%s%s" % (number, number, number))
result = m1 + m2 + m3   
print("The result is: ", result)