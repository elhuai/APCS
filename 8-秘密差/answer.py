x = int(input('輸入一個 十進位正整數'))
odd = 0  #奇數和預設初始值為0
even = 0 #偶數和預設初始值為0

i=1
while x!=0:
    d = x%10 #取出最後一位數
    if i % 2 == 0: #如果是偶數位
        even += d #將數字加到偶數和
    else: #如果是奇數位
        odd += d #將數字加到奇數和
    x /= 10 #去掉最後一位數
    i += 1 
 
diff = odd-even #計算奇數和減去偶數和
if diff < 0: #如果diff小於0，取絕對值
    diff *= -1 

print(diff)