str1=input ("Enter the numbers in list")
lst=str1.split() 
"""Creates a list of numbers entered by splitting"""
print(lst)
sum=0
for i in lst:
	sum=sum+int(i)
	"""Calculates sum by adding every number in the list"""
print(sum)