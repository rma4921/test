test=[]

for i in range(9):
    data = int(input("숫자를 입력해주세요: "))
    test.append(data)
    
mpoint = max(test)
print(mpoint)
print(test.index(mpoint) + 1)
