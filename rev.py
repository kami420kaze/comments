data = []
num = 0
i = 1

with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		num += 1
		if num == 1000 * i: #老師的寫法 num % 1000 == 0
			print(len(data)) # % 是求「餘數」符號 ex 7 % 3 = 1
			i += 1

print('讀完了啦累死,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)

avg_len = sum_len / num
print(avg_len)