datas = []
testData = []
result = 0

with open("Day7.txt", "r") as file:
    for line in file:
        testData.append(line)
        datas.append(line.strip().split(":"))
        
def recursive(target, curSum, arr):
        
    if curSum == target and arr == []:
        return True
    
    if len(arr) == 0:
        return

    if recursive(target, curSum + int(arr[0]), arr[1:]):
        return True
    
    if recursive(target, curSum * int(arr[0]), arr[1:]):
        return True
    
    return False

for data in datas:
    
    target = int(data[0])
    numbers = list(map(int, data[1].strip().split()))
    
    if recursive(target, numbers[0], numbers[1:]):
        result += target

print(result) # 303876485655

################### part 2 ###########################


def recursive2(target, curSum, arr):
        
    if curSum == target and arr == []:
        return True
    
    if len(arr) == 0:
        return

    if recursive2(target, curSum + int(arr[0]), arr[1:]):
        return True
    
    if recursive2(target, curSum * int(arr[0]), arr[1:]):
        return True
    
    if recursive2(target, int(str(curSum) + str(arr[0])), arr[1:]):
        return True
    
    return False

res2 = 0    
for data in datas:
    
    target = int(data[0])
    numbers = list(map(int, data[1].strip().split()))

    if recursive2(target, numbers[0], numbers[1:]):
        res2 += target
    
print(res2)
        
        


    