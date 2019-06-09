#Take numbers and add to list and tuple
a=input("Enter a series of numbers seperated by commas")
list=a.split(",")
tu=tuple(list)
print(tu)


'''
# IF list is to contain integers
a=input("Enter a series of numbers seperated by commas")
list=a.split(",")
list2=[]
for i in list:
  list2.append(int(i))
print(list2)
tu=tuple(list2)
print(tu)

'''