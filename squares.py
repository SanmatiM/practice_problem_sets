n=eval(input("Enter the number till which squares need to calculated"))
num=[]
d=dict()
square=[]
for n in range (1,n):
	num.append(n)
	square.append(n**2)
	d=dict(zip(num,square))
print(d)