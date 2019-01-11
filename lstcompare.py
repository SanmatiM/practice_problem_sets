lst1=[]
lst2=[]
lst1.extend(eval(input("Enter numbers in list1")))
lst2.extend(eval(input("Enter numbers in list2")))
for i in range(0,len(lst1)):
	for j in range(0,len(lst2)):
		if (lst2[j]==lst1[i]):
			print ("True")
		break

else:
	print("False")