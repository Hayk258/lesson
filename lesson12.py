import random

point = 0
while True:
	if point == 20:
		user = int(input("please enter  1"))
		if user == 1:
			point += user
			print(point,user,"win pc")
			break
	else:
		user = input("please enter betwen 1-3 ")
		if user.isdigit():
			user = int(user)
			if user > 0 and user < 4:
				point += user
				print(user,point)
			else:
				print("please input 1-3")
		else:
			print("please input number ")


		if point >= 21:
			print("win pc",point)
			break



		pc = random.randint(1,3)
		if point > 0 and point < 4:
			pc = 4 - point
		if point > 4 and point < 8:
			pc = 8 - point
		if point > 8 and point < 12:
			pc = 12 - point
		if point > 12 and point < 16:
			pc = 16 - point
		if point > 16 and point < 20:
			pc = 20 - point
		elif point == 20:
			pc = 1

		point += pc
		print(pc,point)
		if point == 21:
			print("win user",point)
			break
