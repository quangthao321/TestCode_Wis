def KiemTraSoNguyenTo(n):
    if (n == 2 or n == 3):
        print('Đây là số nguyên tố')
    a = int(n/2)
    for i in range(2,a+1):
        if n%i == 0:
            print('Đây không phải là số nguyên tố')
            break
        else:
            if i == a:
                print('Đây là số nguyên tố')
            continue

b = int(input('Hãy nhập vào một số: '))
KiemTraSoNguyenTo(b)

