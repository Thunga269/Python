#Cho dãy số nguyên A[] gồm có N phần tử. 
# Nhiệm vụ của bạn là tìm dãy số B[] có tổng phần tử nhỏ nhất thỏa mãn tính chất A[i] / B[i] = A[i+1] / B[i+1] 
# với mọi chỉ số i (0 ≤ i ≤ N-2).
def check(p) :
    for i in a:
        if int(i / p) == int(i / (p + 1)) :
            return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
s, ans = min(a), 0
for i in range(s, 0, -1) :
    if check(i) :
        for j in range(n) :
            ans += int(a[j] / (i + 1)) + 1
        break
print(ans)