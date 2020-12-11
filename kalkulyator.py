print (5 * 5)
print (5 % 5)
print(25 + 10 * 5 * 5)
print(150 / 140)
print(10*(6+19)) 
print(5**5)   #aysinqn 5i 5 astichan
print(8**(1/3))
print(20%6)
print(10//4)
print(20%6)   #cuyca talis vor 20 bajanes 6 taki ostatken inchqana mnalu



while True:
	x = input("num1  ")
	y = input('num2  ')
	if x.isdigit() and y.isdigit():
		x = float(x)
		y = float(y)
		break
	else:
		print('please input number')

choise = input("+ - * /")
if choise == '+':
	print(x+y)
elif choise == '-':
	print(x-y)	
if choise == '/':
	print(x/y)
elif choise == '*':
	print(x*y)