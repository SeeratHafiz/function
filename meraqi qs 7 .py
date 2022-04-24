# # isEven()

# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()




# def greet(names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender")







# def info(name, age ="12"):
#        print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")



# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","seerat")

# def add_numbers():
#     num1 = 56
#     num2 = 12
#     add_numbers(num1,num2)
# add_numbers()



# list=[11,5,17,18,23]
# i=0
# while(i<len(list)):
#     total=total+list[i]
# i=i+1
# print("sum of all elements in given list",total)



s=5
i=1
while i<=5:
    j=1
    while j<=5:
        if j<i:
            print(i,end="")
        else:
            print(j,end="")
        j=j+1
        print()
        s=s+1
        i=i+1

