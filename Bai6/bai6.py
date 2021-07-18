def TinhGiaiThua(n):
    if n==0:
        return 1
    else:
        return n * TinhGiaiThua(n-1)

n = int(input('Hãy nhập số cần tình giai thừa: '))

if n > -1:
    print('Kết quả là: ', TinhGiaiThua(n))
