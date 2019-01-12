def filterfn():
	num=[]
	filterdlst=[]
	n=int(input("Enter number of elements in the list"))
	for i in range(1,n+1):
		k=input("Enter the number %d to be added to the list" %i)
		num.append(k)
	for numb in num:
		if int(numb)%2==0:
			filterdlst.append(numb)
	print(filterdlst)

filterfn()

