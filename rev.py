import random
data = []
num = 0
i = 1
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		num += 1
		if num == 10000 * i: #老師的寫法 num % 1000 == 0
			print(len(data)) # % 是求「餘數」符號 ex 7 % 3 = 1
			i += 1

print('讀完了啦累死,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)

avg_len = sum_len / num
print('平均評論長度為', avg_len, '字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d.strip())
print('總共有', len(new), '筆資料小於100字')

shit = []
for d in data:
	if 'shit' in d:
		shit.append(d.strip())
x = (len(shit))
r = random.randint(0, x)
print('一共有', len(shit), '人覺得這個產品很shit')
print('有人說:', shit[r])
print('這是其中的第', r, '筆')