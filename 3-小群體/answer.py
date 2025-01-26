n = int(input("輸入團體中人數"))
friends = [int(x) for x in  input("輸入好友列表").split()] #將好朋友的列表存成串列
mark = [0]*n #標註有沒有被找過
group = 0 

# 從 0 號開始找起
for i in range(n):
    if  mark[i] ==1:   #找過就跳過
        continue
    
    mark[i] = 1 #找過先標記
    nf = friends[i] #找i的好朋友 存到nf變數裡
    group += 1

    while nf != i:
    #再去找好朋友的朋友
        mark[nf] = 1 #找過先標記
        nnf = friends[nf] #找nf的好朋友 存到nnf變數裡
        nf = nnf   #將nnf存到nf變數裡

print(group) #輸出有幾個團體

