
def fibonacci(n):
    if n < -1:
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

x = int(input('Bạn muốn in bao nhiêu số trong dãy fibonacci? '))
st = ''
for i in range(0,x):
    st = st + str(fibonacci(i)) + ', '
print('Dãy fibonacci bạn muốn là: ',st)