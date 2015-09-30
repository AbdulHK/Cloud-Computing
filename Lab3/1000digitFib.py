def fib(n):
	a,b= 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

n=1
while True:
	f=fib(n)
	if len(str(f)) >=1000:
		print("#%d: %d" % (n,f))
		exit()
	n +=1	