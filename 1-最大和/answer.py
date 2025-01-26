N, M = map(int, input("請輸入第一行的兩正整數資料").split())  # 從輸入中讀取兩個整數 N 和 M
maxNum = []  # 初始化存放每行最大值的列表
divisible = []  # 初始化存放可被 MaxSum 整除的數字列表

for i in range(N):  # 循環 N 次，讀取每行數據
    inputarray = list(map(int, input("輸入每行數據").split()))  # 將輸入的一行轉換為整數列表
    maxNum.append(max(inputarray))  # 將該行的最大值添加到 maxnum 列表中

MaxSum = sum(maxNum)  # 計算 maxnum 列表的總和
print(MaxSum)  # 輸出 MaxSum 的值

for j in maxNum:  # 遍歷 maxnum 列表中的每個元素
    if MaxSum % j == 0:  # 如果 MaxSum 能被該元素整除
        divisible.append(j)  # 將該元素添加到 divisible 列表中


if divisible == []:  # 如果 divisible 列表為空
    print("-1")  # 輸出 -1
else:  # 否則
    print(*divisible)  # 將 divisible 列表中的元素以空格分隔輸出
