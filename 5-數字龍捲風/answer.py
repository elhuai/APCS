n = int(input("幾維串列（幾乘幾）"))  # 讀取串列的大小，串列為 n x n 的方陣
array = []  # 用來存放主串列
temp = []  # 臨時清單，用來存放每行輸入後的內容
direction = int(input("讀取方向 0左 、1上 、2右 、3下 "))  # 讀取方向的設定 (0, 1, 2, 3)

for i in range(n):  # 依次讀取串列的每一行
    temp = list(input("每行的串列內容"))  # 將輸入的每行轉換為字元清單
    for j in range(len(temp)):  # 移除清單中的空格
        if " " in temp:
            temp.remove(" ")  
    array.append(temp)  # 將處理後的清單加入主串列 array

positionx = int((n - 1) / 2)  # 設定起始位置 x 為串列的中心
positiony = int((n - 1) / 2)  # 設定起始位置 y 為串列的中心

if direction == 0 or direction == 1:  # 根據方向設定步伐 diff 的初始值
    diff = 1  # 如果方向是 0 或 1，步伐為正方向
else:
    diff = -1  # 如果方向是 2 或 3，步伐為反方向

print(array[positiony][positionx], end="")  # 輸出起始位置的元素，無換行

for i in range(1, n + 1):  # 開始螺旋移動，i 表示步數層數
    if direction == 0 or direction == 2:  # 若方向為水平優先 (0 或 2)
        for j in range(i):  # 往水平方向移動 i 步
            positionx = positionx - diff  # 調整 x 位置
            if positionx < 0 or positiony < 0 or positionx >= number or positiony >= number:
                break  # 若超出串列範圍，跳出循環
            print(array[positiony][positionx], end="")  # 輸出當前位置元素
        for k in range(i):  # 往垂直方向移動 i 步
            positiony = positiony - diff  # 調整 y 位置
            if positionx < 0 or positiony < 0 or positionx >= number or positiony >= number:
                break  # 若超出串列範圍，跳出循環
            print(array[positiony][positionx], end="")  # 輸出當前位置元素
        diff = diff * (-1)  # 反轉方向

    elif direction == 1 or direction == 3:  # 若方向為垂直優先 (1 或 3)
        for k in range(i):  # 往垂直方向移動 i 步
            positiony = positiony - diff  # 調整 y 位置
            if positionx < 0 or positiony < 0 or positionx >= number or positiony >= number:
                break  # 若超出串列範圍，跳出循環
            print(array[positiony][positionx], end="")  # 輸出當前位置元素
        for j in range(i):  # 往水平方向移動 i 步
            positionx = positionx + diff  # 調整 x 位置
            if positionx < 0 or positiony < 0 or positionx >= number or positiony >= number:
                break  # 若超出串列範圍，跳出循環
            print(array[positiony][positionx], end="")  # 輸出當前位置元素
        diff = diff * (-1)  # 反轉方向
