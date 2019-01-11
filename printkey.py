dict1={1:"Speckbit", 2:"World", 3:"Quiet"}
"""A dictionary in which we want to search a value"""

search=input("Enter the word to be searched")
"""Value which needs to be searched in dictionary"""
for key in dict1:  #Traverse through the dictionary
	if dict1[key]== search:
		print("Key is %d" % key)
		
