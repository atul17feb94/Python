#program to enter 5  elements from user in an empty list

newlist=[]    
print("Enter the numbers: ")

for i in range(0,5):
    number=input()
    newlist.append(number)
    
print(newlist)
