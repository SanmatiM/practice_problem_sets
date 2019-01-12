lst=[]
strg=input("Enter the elements")
lst=strg.split()
search=input("Enter the element to be searched")
for ele in lst:
	if ele==search:
		print("True")
		break
else:
	print("False")