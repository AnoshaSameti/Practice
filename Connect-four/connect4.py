def who_is_winner(pieces_position_list):
    board=[[0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]
           ]
    listp=[]
    listc=[]
    add=0

    for i in pieces_position_list:
        listp.append(i[:1])
        listc.append(i[2:])

    for i in range(len(pieces_position_list)):
        if listc[i]=='Yellow':
            listc[i]=1
        else:
            listc[i]=2

    for i in range(len(pieces_position_list)):
        if listp[i]=='A':
            listp[i]=0
        elif listp[i]=='B':
            listp[i]=1
        elif listp[i]=='C':
            listp[i]=2
        elif listp[i]=='D':
            listp[i]=3
        elif listp[i]=='E':
            listp[i]=4
        elif listp[i]=='F':
            listp[i]=5
        elif listp[i]=='G':
            listp[i]=6

    def check(board):
        for i in range(6):
            for j in range(7):
                if board[i][j] == 0:
                    continue
                if i<=2:
                    if board[i+3][j] == board[i][j] and board[i][j] == board[i+1][j] and board[i][j]==board[i+2][j]:
                        return board[i][j]
                if j<=3:
                    if board[i][j+3]==board[i][j] and board[i][j] == board [i][j+1] and board[i][j]==board[i][j+2]:
                        return board[i][j]
                if i<=2 and j<=3:
                    if board[i+1][j+1]==board[i][j] and board[i][j]==board[i+2][j+2] and board[i][j]==board[i+3][j+3]:
                        return board[i][j]
                if i>=3 and j<=3:
                    if board[i][j]==board[i-1][j+1] and board[i][j]==board[i-2][j+2] and board[i][j]==board[i-3][j+3]:
                        return board[i][j]


    for j in listp:
        inx=listp.index(j,add)
        add=inx+1
        for i in range(5,-1,-1):
            if board[i][j] == 0:
                board[i][j]=listc[inx]
                break
        winner = check(board)
        if winner == 1:
            return 'Yellow'
        elif winner == 2:
            return 'Red'
    return 'Draw'