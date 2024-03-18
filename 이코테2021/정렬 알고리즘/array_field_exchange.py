# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

n, k = 5, 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]

a.sort()
b.sort(reverse=True)

for i in range(k):
    if (a[i]<b[i]):
        a[i], b[i] = b[i], a[i]

print(sum(a))