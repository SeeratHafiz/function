# i=0
# sum=0
# while i<=100:
#     if i<=sum:
#         sum=sum+1
#     i=i+1
#     print(sum)


# i=1
# while i<=100:
#     if i%3==0 and i%7==0:
#          print(i,"Navgurukul")
#     elif i%3==0:
#          print(i,"Nav")
#     elif i%5==0:
#         print(i,"Gurukul")
#     else:
#             print(i,"unknown")
#     i=i+1

# i=1
# sum=0
# while i<=10:
#     a=int(input("enter the no.:"))
#     sum=sum+a
#     i=i+1
# print(sum)

# num=int(input("enter the number:"))
# count=0
# i=1
# while i<num:
#     if num%i==0:
#      count+=1
#     i=i+1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number")

# a=int(input("enter the number:"))
# fac=1
# while a>=0:
#     fac=fac*a
#     i=i-1
#     print("factorial=,fact")

# i=12
# sum=0
# while i<=421:
#     sum=sum+i
#     print(sum)
#     i=i+1

# i=30
# while i<=420:
#     if i%8==0:
#         print(i)
#     i=i+1

# i=1
# while i<=10:
#     print(i**2)
#     i=i+1

# i=1
# a=int(input("enter the number:"))
# while i<=10:
#     print(i*a)
#     i=i+1


# num=int(input("enter the number:"))
# i=1
# sum=0
# while i<=1:
#     a=num%10
#     b=(num//10)%10
#     c=(num//100)%10
#     a=a**3
#     b=b**3
#     c=c**3
#     i=i+1
#     sum=a+b+c
# if sum==num:
#     print(sum,"it is an armstrong number")
# else:
#     print(sum,"it is not an armstrong number")

# i=10
# while i>=1:
#     print(i)
#     i=i-1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1



# i = 891
# while i < 931:
#     z = i - 890
#     if z % 3 == 0:
#         print(z)
#     i = i + 1


# i = 0
# while i <= 50:
#   if i != 0:
#       print(i)
#   i = i + 5




# i = 49
# while i <= 98:
#   i = i + 2
#   print(i)



# i = 50
# while i <= 100:
#   if i % 2 != 0:
#       print(i)
#   i = i + 1

# i = 400
# while i >= 350:
#   z = i - 300
#   if z % 2 != 0:
#       print(z)
#   i = i - 1


index = 0;  
while 1:  
    print(index," ",end = ""),  
    index=index+1;  
    if index == 10:  
        break;  
print("Found at",index,"location")