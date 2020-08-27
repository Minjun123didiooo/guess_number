#產生一個隨機整數1~100 讓使用者重複輸入數字去猜
#若猜對 印出'猜對了!'
#若猜錯 印出'比答案大/小'

import random
start = input('請決定隨機數字範圍開始值: ')
start = int(start)
end = input('請決定隨機數字範圍結束值: ')
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count = count + 1
	number = input('請猜一個數字: ')
	number = int(number)
	if number == r:
			print('你猜中了!')
			print('這是你猜的第', count, '次')
			break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
	print('這是你猜的第', count, '次')