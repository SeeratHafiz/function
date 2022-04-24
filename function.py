# def add(a,b):
#  c=a+b
#  return c
# a=int(input("enter 1st no:"))
# b=int(input("enter 2nd no:"))
# add(a,b)



# def add(a,b):
#     c=a+b
#     return c
# a=int(input("enter 1st no:"))
# b=int(input("enter 2nd no:"))
# add(a,b)



# def foo(hello, *args):
#     print hello

#     for each in args:
#         print each

# if __name__ == '__main__':
#     foo("LOVE", ["lol", "lololol"])



# def xyz(s,n):
#     if n==0:
#         print(s[0])
#     else:
#         print(s[n],end=" ")
#         xyz (s,n-1)
# s=input("enter string")
# xyz(s,len(s)-1)



# def findpower(x,y):
#     if y==0:
#         return 1
#     else:
#         return(x*findpower(x,y-1))
# x=int(input("enter base"))
# y=int(input("enter exponent"))
# z=findpower(x,y)
# print("calculated value")


mylist=["python","hub"]
for i in mylist:
    mylist.append(i.upper())
print(mylist)