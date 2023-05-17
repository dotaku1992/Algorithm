import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
print("INVALID" if arr.count(0) != 0 and arr.count(0) >= len(arr) / 2 else "APPROVED" if arr.count(1) > arr.count(-1) else "REJECTED")
