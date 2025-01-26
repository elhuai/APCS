
playerlist=[]

for i in range(9):
    players = input("請輸入資料")
    playertemplist = players.split(" ")
    # print(playertemplist)
    for j in range(len(playertemplist)):
        if playertemplist[j]==" ":
            playertemplist.remove(" ")
    playerlist.append(playertemplist)

'''列出方便測試
playerlist.append(['5','1B','1B','FO','GO','1B'])
playerlist.append(['5','1B','2B','FO','FO','SO'])
playerlist.append(['4','SO','HR','SO','1B'])
playerlist.append(['4','FO','FO','FO','HR'])
playerlist.append(['4','1B','1B','1B','1B'])
playerlist.append(['4','GO','GO','3B','GO'])
playerlist.append(['4','1B','GO','GO','GO'])
playerlist.append(['4','SO','GO','2B','2B'])
playerlist.append(['4','3B','GO','GO','FO'])
for i in range(len(playerlist)):
	print(playerlist[i])
'''
	

out_b = int(input())  # 輸入允許的總出局數（out_b）
out = 0  # 初始化當前出局數為0
step = 0  # 初始化擊球結果的步數（上幾壘）
steplist = [0, 0, 0, 0]  # 跑壘情況列表，[得分, 一壘, 二壘, 三壘]


for i in range(len(playerlist)):  # 外層迴圈，遍歷每個擊球回合
    for j in range(9):  # 內層迴圈，遍歷每個球員
        if i < int(playerlist[j][0]):  # 檢查球員是否有第i+1次擊球
            if playerlist[j][i+1] == "SO":  # 如果是三振出局
                out += 1  # 出局數加1
            elif playerlist[j][i+1] == "FO":  # 如果是飛球出局
                out += 1  # 出局數加1
            elif playerlist[j][i+1] == "GO":  # 如果是滾地球出局
                out += 1  # 出局數加1
            else:  # 如果不是出局，則處理擊球結果
                step = playerlist[j][i+1].split('B')  # 分割擊球結果，例如"1B"變為["1", ""]
                if step[0] == "HR":  # 如果是本壘打
                    steplist[0] += 1  # 得分加1
                    for k in range(1, 4):  # 檢查壘上的跑者
                        if steplist[k] == 1:
                            steplist[0] += 1  # 每有一個跑者，得分加1
                            steplist[k] = 0  # 清空該壘位
                else:
                    d = int(step[0])  # 取得擊出的壘數（例如1B的1）
                    for k in range(3, 0, -1):  # 從三壘到一壘遍歷
                        if steplist[k] == 1:
                            steplist[k] = 0  # 清空原壘位
                            if k + d > 3:  # 如果跑者超過三壘
                                steplist[0] += 1  # 得分加1
                                continue  # 繼續下一個跑者
                            steplist[k + d] = 1  # 跑者移動到新的壘位
                    steplist[d] = 1  # 新的打者上壘
            print(playerlist[j][i+1], out, steplist)  # 輸出當前狀態
            
            if out >= 3:  # 如果出局數達到3
                out = 0  # 重置出局數
                out_b -= 3  # 減少總出局限制
                for k in range(1, 4):
                    steplist[k] = 0  # 清空所有壘位
                    
            #跳出回圈的條件        
            if out == out_b:  # 如果出局數達到輸入的限制
                break  # 結束迴圈
print("score=", steplist[0])  # 輸出最終得分

