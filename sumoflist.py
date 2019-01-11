lst=[]
lst.extend(eval(input ("Enter the numbers in list")))

"""Creates a list of numbers entered by splitting"""
print(lst)
sum=0
for i in lst:
	sum=sum+int(i)
	"""Calculates sum by adding every number in the list"""
print(sum)