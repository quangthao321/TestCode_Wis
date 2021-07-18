string = input('Nhập vào một chuỗi: ')
newstring = string[::-1]
#print(string)
#print(newstring)
if string == newstring:
    print('Chuỗi đó là chuỗi palindrome')
else:
    print('Chuỗi đó không phải là chuỗi palindrome')

for i in range(1,10):
    if i%2==0:
        print(i,end=',')



