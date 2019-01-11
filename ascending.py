lst=[]
n=int(input("Enter number of elements to be sorted"))
for i in range(1,n+1):
	inp=int(input("Enter the %i number to be arranged in ascending order" %i))
	lst.append(inp)
lst.sort()
print(lst)