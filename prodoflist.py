lst=[]
lst.extend(eval(input ("Enter the numbers in list")))

"""Creates a list of numbers entered by splitting"""
print(lst)
prod=1
for i in lst:
	prod*=int(i)
	"""Calculates product by multiplying every number in the list"""
print(prod)