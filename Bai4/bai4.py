while True:
    inp = list(map(str, input("Nhập các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ").split(",")))
    #bien được dùng để kiểm tra xem số nhập vào có là số nhị phân 4 chữ số hay không
    bien=0
    for item in inp:
        if len(item) != 4:
            bien=1
    if bien==0:
        for i in range(len(item)):
            if item[i] != '0' and item[i] != '1':
                bien=1
                break
    if bien==0:
        break
    else:
        print('Hãy nhập lại')

for num in inp:
    if int(num)%5 == 0:
        print(num, end='')
