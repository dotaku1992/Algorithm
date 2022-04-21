import sys

n = int(sys.stdin.readline().rstrip())
student = [float(sys.stdin.readline().rstrip()) for _ in range(n)]
student.sort()
for val in student[:7]:
    print(f"{val:.3f}")
