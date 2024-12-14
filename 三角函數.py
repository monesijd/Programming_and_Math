import math
    
my_factorial = [1]
for num in range(1, 151):
    my_factorial.append(num * my_factorial[num-1])
# 建立階乘表

def sin(x):
    answer = 0
    for _ in range(1, 151, 2):
        if _ % 4 == 1:
            answer += (x**(_) / my_factorial[_])
        else:
            answer -= (x**(_) / my_factorial[_])
    return answer
# 將 sin 函數在 x = 0 做泰勒展開式，算出近似值

def cos(x):
    answer = 0
    for _ in range(0, 150, 2):
        if _ % 4 == 0:
            answer += (x**(_) / my_factorial[_])
        else:
            answer -= (x**(_) / my_factorial[_])
    return answer
# 將 cos 函數在 x = 0 做泰勒展開式，算出近似值

pi = math.pi
x = float(input("Please input x: "))
if x > pi or x < -pi:
    x = x % (2*pi)

print(f"sinx = {sin(x):.11f}")
print(f"cosx = {cos(x):.11f}")
