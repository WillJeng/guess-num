import random

r = random.randint(1, 100)
while True:
	num = input("請輸入1到100的終極數字:")
	num = int(num)
	if num == r:
		print("恭喜猜中")
		break
	elif num > r:
		print("在小一點")
	elif num < r:
		print("在大一點")