my_factorial = [1]
for num in range(1, 151):
    my_factorial.append(num * my_factorial[num-1])
# 建立階乘表

def e():
    answer = 0
    for each_number in my_factorial:
        answer += (1 / each_number)
    return answer
# 利用尤拉函數做泰勒展開，算出e的近似值

print(f"e = {e()}")
