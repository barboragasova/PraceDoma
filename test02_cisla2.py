#Phase one
    #multiplication and even/odd check

a = (5)
b = (6)

print(a*b)

if a*b % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")

a2 = (4)
b2 = (9)

print(a2*b2)

if a2 * b2 % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")

#Phase two
    #division check

if a*b % 6 == 0 and a2*b2 % 6 == 0:
    print("The numbers are divisible by 6.")