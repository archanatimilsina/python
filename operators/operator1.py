# # Arithmetic Operator
# a=30
# b=5

# # +
# print(a+b) #output: 35


# # -
# print(a-b) #output:25


# # *
# print(a*b) #output: 150


# # /
# print(a/b) #output: 6.0


# # **
# print(a**b) #output: 24,300,000 


# # //
# x=7
# y=2
# print(x//y) #output:3 (3.5 gives 3)


#  # %
# print(a%b) #output:0 (remaining value)


#Assignment operator
# a,b= 30,5

# #     =
# m=a
# n=b
# print(m+n) #output: 35
# # Background: m=30 , n=5 m+n= 30+5=35


# #     +=
# a+=b
# print(a) #output: 35
# # Background: a=a+b  ;  a=30+5 so a=35


# #     -=
# a-=b
# print(a) #output: 25
# # Background:  a=a-b  ;  a=30-5 so a=25


# #     *=
# a*=b
# print(a) #output: 150
# # Background:  a=a*b  ;  a=30*5 so a=150


# #     /=
# a/=b
# print(a) #output: 
# # Background: a=a/b  ;  a=30/5 so a=6.0


# a=9
# b=2
# #     //=
# a//=b
# print(a) #output: 
# # Background: a=a//b  ;  a=9//2 so a=4


# #     **=
# a**=b
# print(a) #output: 
# # Background:  a=a**b  ;  a=9**2 so a=81



# #     %=
# a%=b
# print(a) #output: 
# # Background:  a=a%b  ;  a=9%2 so a=1


# #     &=→ Bitwise AND assignment 
# a = 5  # in binary: 0101
# b = 3  # in binary: 0011

# a &= b  # a = a & b
# print(a)  # Output: 1 (binary: 0001)


# #     |= → Bitwise OR assignment
# a = 5  # 0101
# b = 3  # 0011

# a |= b  # a = a | b
# print(a)  # Output: 7 (0111)


# #     ^= → Bitwise XOR assignment
# # This operator performs a bitwise XOR and updates the left-hand variable.
# a = 5  # 0101
# b = 3  # 0011

# a ^= b  # a = a ^ b
# print(a)  # Output: 6 (0110)



# #     >>= → Right shift assignment
# a = 8  # 1000
# a >>= 2  # shift right by 2 bits
# print(a)  # Output: 2 (0010)



# #     <<= → Left shift assignment
# a = 3  # 0011
# a <<= 2  # shift left by 2 bits
# print(a)  # Output: 12 (1100)



# #     := → Walrus operator (assignment expression)

# n = len([1, 2, 3])
# if n > 2:
#     print(f"List is too long, length = {n}")
# #    instead of above multiple lines we can do this 

# if (n := len([1, 2, 3])) > 2:
#     print(f"List is too long, length = {n}")


#comparision operator
# == 
# a,b=5,5
# if(a==b):
#   print("a is equal to b")
# else:
#   print("a is not eqaul to b")

# a,b=5,"5"
# if(a==b):
#   print("a is equal to b")
# else:
#   print("a is not eqaul to b")

# !=
# a,b=5,10
# if(a!=b):
#   print("a is not equal to b")
# else:
#   print("a is eqaul to b")

a,b=5,10
#. >
print(a>b) #output: False
#. <
print(a<b) #output: True

#. <=
print(a<=b)#output: True 

#. >=
print(a>=b)#output: False

