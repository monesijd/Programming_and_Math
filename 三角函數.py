import math
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return factorial(num-1) * num
my_factorial = [1]
for _ in range(1, 151):
    my_factorial.append(factorial(_))
# 建立階乘表

def sin(x):
    answer = 0
    for _ in range(1, 151, 2):
        if _ % 4 == 1:
            answer += (x**(_) / my_factorial[_])
        else:
            answer -= (x**(_) / my_factorial[_])
    return answer
# 將sin函數在x=0做泰勒展開式，算出近似值

def cos(x):
    answer = 0
    for _ in range(0, 150, 2):
        if _ % 4 == 0:
            answer += (x**(_) / my_factorial[_])
        else:
            answer -= (x**(_) / my_factorial[_])
    return answer
# 將cos函數在x=0做泰勒展開式，算出近似值

pi = math.pi
print("Please input x: ", end="")
x = float(input())
if x > pi or x < -pi:
    x = x % (2*pi)

print(f"sinx = {sin(x):.11f}")
print(f"cosx = {cos(x):.11f}")