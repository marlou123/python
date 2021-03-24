import math
a= float(input("Input one leg of the triangle: 2"))
b= float(input("Input one leg of the triangle: 3"))
#Step 1: square x
a= a*a
#Step 2: square y
b= b*b
#step 3: add x and y and store in a temp variable
temp= a + b
#Step 4: take square root of temp 
r= math.sqrt(temp)
print("A right triangle with side lenghts",a,","b," will have hypothenuse of ",r)
