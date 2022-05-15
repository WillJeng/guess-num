import random
start = input("請輸入你要的起始值:")
end = input("請輸入你要的最終值")
start = int(start)
end = int(end)
count = 0
r = random.randint(start, end)
while True:
	count = count + 1 #i += 1 
	num = input("請輸入1到100的終極數字:")
	num = int(num)
	if num == r:
		print("恭喜你在第", count, "次", "猜中了")
		break
	elif num > r:
		print("在小一點")
	elif num < r:
		print("在大一點")
	print("您已經猜了", count, "次")
