arth = 0
x = 0
val = None
for i in range(n-1):
	if (a[i+1]-a[i]==val):
		x += 1
	else:
		val = a[i+1]-a[i]
		if x > 2:
			arth += (x-1)*(x-2) / 2 #chyba
		x = 2

if x > 2:
	arth += (x-1)*(x-2) / 2 #chyba