t = int(input())
stoidx = {'S': 0, 'R': 1, 'P': 2}

table = [[(0, 0), (1, 0), (0, 1)],
         [(0, 1), (0, 0), (1, 0)],
         [(1, 0), (0, 1), (0, 0)]]

for _ in range(t):
    n = int(input())
    player1score, player2score = 0, 0

    for _ in range(n):
        player1, player2 = input().split()
        s1, s2 = table[stoidx[player2]][stoidx[player1]]
        player1score, player2score = player1score + s1, player2score + s2
    print("TIE" if player1score == player2score else "Player 1" if player1score > player2score else "Player 2")
