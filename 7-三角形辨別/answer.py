a, b, c = sorted(map(int, input("輸入三個數").split()))  # 從使用者輸入三個數字，由小到大安排分別賦值給 a, b, c
print(a, b, c)  
if a + b <= c:  # 如果最短兩邊的和小於或等於最大邊，則無法形成三角形
    print('No')  
elif a * a + b * b < c * c:  # 如果平方和小於最大邊平方，則為鈍角三角形
    print('Obtuse')  
elif a * a + b * b == c * c:  # 如果平方和等於最大邊平方，則為直角三角形
    print('Right')  
else:  # 如果平方和大於最大邊平方，則為銳角三角形
    print('Acute')  