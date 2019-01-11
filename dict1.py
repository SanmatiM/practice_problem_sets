dict1={1:"Speckbit", 2:"World", 3:"Quiet"}
search=input("Enter the word to be searched")
for key in dict1:
	if dict1[key]== search:
		print("True")
		break
else:
		print("False")