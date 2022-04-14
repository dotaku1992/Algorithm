import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    person = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    max_cnt = max(person)
    winner_cnt = 0
    for val in person:
        if max_cnt == val: winner_cnt += 1
    if winner_cnt > 1:
        print("no winner")
    else:
        flag = (sum(person) / 2) < max_cnt
        print(f"{'majority' if flag else 'minority'} winner {person.index(max_cnt) + 1}")
