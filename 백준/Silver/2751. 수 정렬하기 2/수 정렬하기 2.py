import sys
input = sys.stdin.readline

t = int(input())

arr = []

for _ in range(t):
    arr.append(int(input()))

arr = sorted(arr)

for i in arr:
    print(i)