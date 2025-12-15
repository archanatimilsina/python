# while loop
# i=1
# while i<=10:
#     print(i)
#     if i==8:
#         break
#     i+=1
#output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

#continue Skip the rest of this loop iteration and jump back to the top. and it checks condition if it is true
# i=1
# while i<=10:
#     i+=1
#     if i==8:
#         continue
#     print(i)
#output : 
# 2
# 3
# 4
# 5
# 6
# 7
# 9
# 10
# 11

# i=1
# while i<=10:
#     if i==8:
#         continue
#     print(i)
#     i+=1
#output : infinite loop bcz the value of i hasn't changed so it will keep getting 8 and continue current loop

#else statement = we can run a block of code once when the condition no longer is true
i=1
while i<=10:
    i+=1
    if i==8:
        continue
    print(i)
else: 
    print("loop completed!!!")

#output :
# 2
# 3
# 4
# 5
# 6
# 7
# 9
# 10
# 11
# loop completed!!!