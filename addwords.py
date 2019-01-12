
def addword():
	n=int(input("Enter number of new words to be added to the list"))
	lst=[]
	for i in range (0,n):
		word=input("Enter the word to be added to list")
		lst.append(word)
	print(lst)


addword()