# 定義四個方向的座標偏移量 (左、上、右、下) [行,列]
around = [[0, -1], [-1, 0], [0, 1], [1, 0]]
'''
around = [[0, -1], [-1, 0], [0, 1], [1, 0]] 表示四個方向的移動：
            
[0, -1] 表示向左一格（列減 1）。
[0, 1] 表示向右一格（列加 1）。
[-1, 0] 表示向上一格（行減 1）。
[1, 0] 表示向下一格（行加 1）。

'''

# 讀取行數 (R)、列數 (C)、分配比例 (k)、遷移輪數 (m)
R, C, k, m = map(int, input().split())

# 建立二維陣列 city 來儲存初始人口數
city = []
for i in range(R):
    city.append(list(map(int, input().split())))  # 將每一行的輸入轉換為整數並加入 city

# 建立與 city 相同大小的陣列 citytemp，用於暫存每輪遷移後的結果
citytemp = [[0 for i in range(C)] for j in range(R)]
print(citytemp)
# 進行 m 輪遷移
for d in range(m):
    for r in range(R):# 進行 行數 (R) 遍歷
        for c in range(C):# 進行 列數 (C) 遍歷
            if city[r][c] == -1:
                citytemp[r][c] = city[r][c]  # 如果是禁區，保持為 -1
            else:
                citytemp[r][c] = city[r][c]  # 初始化 citytemp 為當前人口數
                for i in around:# 去找鄰居的位置
                    aroundx = r + i[0]
                    aroundy = c + i[1]
                    '''
                    假設當前格子位置是 (2, 3)，那麼每個方向的鄰居位置會是：

                   左： i = [0, -1]： aroundx = 2 + 0 = 2，aroundy = 3 - 1 = 2（左邊格子的位置是 (2, 2)）。
                   上： i = [-1, 0]： aroundx = 2 - 1 = 1，aroundy = 3 + 0 = 3（上方格子的位置是 (1, 3)）。
                   右： i = [0, 1]：  aroundx = 2 + 0 = 2，aroundy = 3 + 1 = 4（右邊格子的位置是 (2, 4)）。
                   下： i = [1, 0]：  aroundx = 2 + 1 = 3，aroundy = 3 + 0 = 3（下方格子的位置是 (3, 3)）。
                    '''
                
                    # 檢查鄰居是否在範圍內且不是禁區
                    if 0 <= aroundx < R and 0 <= aroundy < C and city[aroundx][aroundy] != -1:
                        citytemp[r][c] -= city[r][c] // k  # 自己移出的部分人口
                        citytemp[aroundx][aroundy] += city[r][c] // k  # 周圍格子接收移入的人口

    # 更新 city 為 citytemp 的結果
    for r in range(R):
        for c in range(C):  
            city[r][c] = citytemp[r][c]

# 找出最少和最多人口的非禁區格子
minnum = 1000000
maxnum = 0
for r in range(R):
    for c in range(C):
        if city[r][c] != -1:  # 排除禁區
            minnum = min(minnum, city[r][c])
            maxnum = max(maxnum, city[r][c])

# 輸出最少和最多人口
print(minnum)
print(maxnum)
