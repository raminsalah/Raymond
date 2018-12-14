######################################################
# number=eval(input("enter a positive number : "))
# x=2
# while x<=number:
#     for y in range(2,x):
#         if x%y is 0:
#           break
#     else:print(x)
#     x+=1
######################################################
# number=eval(input("enter a number : "))
# ####### print(1769%10)
# ####### print(1769//10)
# while number//10 >= 10:
#     print(number%10 , end="")
#     number=number//10
# print(number%10,end="")
# print(number//10,end="")
#######################################################
######## i=0
######## while number//10>=10:
########     i+=1
########     number=number//10
######## numberOfDigits=i+2
# number=input("enter a number : ")
# stringOfNumber=str(number)
# lenght=len(stringOfNumber)
# sample="2468135790"
# if lenght<10:
#    print("No")
# else:
#     for x in range(0,10):
#         if sample[x] in stringOfNumber:
#           continue
#         else: break
#     if x==9:
#         print("Yes")
#     else:print("no")
#######################################################
## Rectangle
# lenght=int(input("enter the lenght : "))
# width=int(input("enter the width : "))
# for i in range(1, lenght+1) :
#         for j in range(1, width+1) :
#             if (i == 1 or i == lenght or
#                 j == 1 or j == width) :
#                 print("*", end=" ")
#             else :
#                 print(" ", end=" ")
#         print()
#######################################################
## Triangle
Base=int(input("enter an odd number as the base of Triangle : "))
Height=int(input("enter the height of Triangle : "))
for i in range(1,Height+1):
    for j in range(1,Height+1):
        for k in range(1,(Base-Height+1):
           print("&" , end=" ")
        print("*")












