# lambda function ---- to consize 


# addition of two numbers
add=lambda n1,n2:n1+n2
print(add(12,21))

# cube of a number
cube=lambda num:num**3
print(cube(5))

# positive or negative
num_chk=lambda number:"positive" if number>0 else "negative" if number<0 else "zero"
print(num_chk(4))

# largest of two numbers
max_two=lambda num1,num2:num1 if num1>num2 else num2
print(max_two(12,32))

# even or odd
even_odd=lambda num:"even" if num%2==0 else "odd"
print(even_odd(16))


