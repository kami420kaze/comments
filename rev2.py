import random
data = []
num = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        num += 1
        if num % 1000 == 0:
            print(len(data)) # % 是求「餘數」符號 ex 7 % 3 = 1

print('讀完了啦累死,總共有', len(data), '筆資料')

wc = {} # word_count
for d in data:
    words = d.split() # 清單裝著一堆字
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增key進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('妮想查什麼字: ')
	if word == 'quitquitquit':
		break
	if word in wc:
	    print(word, '出現過的次數: ', wc[word])
	else:
		print('沒這個字ㄛQQ')

print('感恩用我寫ㄉ程式xDD')