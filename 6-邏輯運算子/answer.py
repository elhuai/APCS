# 從輸入中讀取三個整數，分別是 a, b, 和 result
# 並將它們轉換成整數型態
a_b_result = list(map(int, input("輸入中a,b,result").split()))

# 初始化一個空的結果列表，用於存儲邏輯運算結果
result_list = []

# 判斷 AND (且) 條件
if a_b_result[0] != 0 and a_b_result[1] != 0:  # 如果 a 和 b 都不為 0，結果為 1
    result_list.append(1)
else:  # 否則，結果為 0
    result_list.append(0)

# 判斷 OR (或) 條件
if a_b_result[0] != 0 or a_b_result[1] != 0:  # 如果 a 或 b 中有一個不為 0，結果為 1
    result_list.append(1)
else:  # 否則，結果為 0
    result_list.append(0)

# 判斷 XOR (異或) 條件
if (a_b_result[0] and not a_b_result[1]) or (not a_b_result[0] and a_b_result[1]):  
    # 當 a 和 b 的值不同 (一個為 0，另一個為 1)，結果為 1
    result_list.append(1)
else:  # 否則，結果為 0
    result_list.append(0)

# 根據結果判斷是 AND、OR、XOR 邏輯運算或不可能的情況
if result_list[0] == a_b_result[2]:  # 如果 AND 結果等於輸入的 result，輸出 "AND"
    print("AND")
if result_list[1] == a_b_result[2]:  # 如果 OR 結果等於輸入的 result，輸出 "OR"
    print("OR")
if result_list[2] == a_b_result[2]:  # 如果 XOR 結果等於輸入的 result，輸出 "XOR"
    print("XOR")
if (
    result_list[0] != a_b_result[2]
    and result_list[1] != a_b_result[2]
    and result_list[2] != a_b_result[2]
):  
    # 如果所有邏輯運算的結果都不等於輸入的 result，輸出 "IMPOSSIBLE"
    print("IMPOSSIBLE")
