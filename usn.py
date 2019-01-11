d=dict()
key=[]
value=[]
n=eval(input("Enter number of keys in dictionary"))
for i in range(n):
	k=input("Enter the usn:")
	v=input("Enter the value:")
	key.append(k)
	value.append(v)
	d=dict(zip(key,value))

print(d)