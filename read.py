#讀取檔案
data =[]
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: #每讀1000筆印出來
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
sum_len = 0
for d in data: #d是用來稱呼每一筆留言的變數名稱
    sum_len += len(d)
print('每一筆留言平均長度為', sum_len / len(data))

#篩選每一筆留言長度小於100個字
new = []
for d in data:
    if len(d) < 100:
        new.append(d.strip())    
print('一共有', len(new), '筆留言，長度小於100')
print(new[0])
print(new[1])

#篩選每一筆留言有提到good
# good = []
# for d in data: #d是用來稱呼每一筆留言的變數名稱
#     if 'good' in d:
#         good.append(d.strip())
# print('一共有', len(good), '筆留言提到good')
# print(good[0])

#清單快寫法
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')
print(good[0])

#也可以把d改成1，表示如果有留言提到good，則把裝進good裡面
# good = [1 for d in data if 'good' in d]
# print(good)
# print('一共有', len(good), '筆留言提到good')

bad = ['bad' in d for d in data]
print(bad)

#原本寫法如下比照line 43
# bad = []
# for d in data:
#     bad.append('bad' in d)
# print(bad)
