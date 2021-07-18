import random

cows = 0
count = 0

def takeANumber():
    while True:
        num = int(input('Hãy nhập số bạn đoán có 4 chữ số: '))
        #print(num)
        if 999 < num < 10000:
            break
    return num

def createANumber():
    value = random.randint(1000,9999)
    return value

value = createANumber()
string_value = str(value)

while True:
    thoat = 0
    count+=1
    num = takeANumber()
    string_num = str(num)
    for i in range(0,4):
        if string_value[i]  == string_num[i]:
            cows+=1
        if cows == 4:
            print('Chúc mừng bạn đã đoán đúng với số lần là ',count)
            thoat = 1
            break
    print('Bạn có ',cows, ' Cows', ' và ',4-cows, 'Bulls')
    if thoat == 1:
        break







