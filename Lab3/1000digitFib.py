#Abdulellah Hakim
def fib(n):
	a,b= 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

n=1
while True:
	f=fib(n)
	#find the string with more than 1000 and prints it
	if len(str(f)) >=1000:
		print(n)
		exit()
	n +=1	