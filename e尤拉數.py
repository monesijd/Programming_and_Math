def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return factorial(num-1) * num
my_factorial = [1]
for _ in range(1, 151):
    my_factorial.append(factorial(_))
# 建立階乘表

def e():
    answer = 0
    for each_number in my_factorial:
        answer += (1 / each_number)
    return answer
# 利用尤拉函數做泰勒展開，算出e的近似值

print(f"e = {e()}")