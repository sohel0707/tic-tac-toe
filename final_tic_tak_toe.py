class Player:
	def __init__(self):
		self.x=-1
		self.y=-1

def isFull(board):
	for i in range(3):
		for j in range(3):
			if board[i][j] == no_move:
				return False
	return True

def evaluate(board):

	for i in range(3):
		if board[i][0] == board[i][1] ==board[i][2]:
			if board[i][0]==opponent:
				return -1
			if board[i][0]==player:
				return 1
		if board[0][i] == board[1][i] ==board[2][i]:
			if board[0][i]==opponent:
				return -1
			if board[0][i]==player:
				return 1
	if board[0][0] == board[1][1] == board[2][2]:
		if board[0][0]==opponent:
			return -1
		if board[0][0]==player:
				return 1
	if board[0][2] == board[1][1] == board[2][0]:
		if board[0][2]==opponent:
			return -1
		if board[0][2]==player:
			return 1
		
	return 0
		 
def findMaxMove(board, depth, isMax):
	eval1 = evaluate(board)
	if eval1!=0:
		return eval1 
	if isFull(board):
		return 0
	if isMax:
		val=-1000
		for i in range(3):
			for j in range(3):
				if board[i][j]==no_move:
					board[i][j]=player
					val=max(val,findMaxMove(board,depth+1,not(isMax)))
					board[i][j]=no_move
		return val
	else:
		val=1000
		for i in range(3):
			for j in range(3):
				if board[i][j]==no_move:
					board[i][j]=opponent
					val=min(val,findMaxMove(board,depth+1,not(isMax)))
					board[i][j]=no_move
		return val



def findBestMove(board):
	val=-1000
	player1=Player()
	player1.x=-1
	player1.y=-1
	for i in range(3):
		for j in range(3):
			if board[i][j] == no_move:
				board[i][j]=player

				temp=findMaxMove(board,0,False)
				board[i][j]=no_move
				if val < temp:
					val=temp
					player1.x=i
					player1.y=j
	return player1

def user_inp(board):
	try:
		user_x, user_y = map(int, input().split())
	except:
		print("the position must be integer")
		user_inp(board)
		return
	if user_x<=0 or user_x>3 or user_y<=0 or user_y >3:
		print("position must be in range 1 to 3")
		user_inp(board)
	elif board[user_x-1][user_y-1] !=no_move:
		print("These cell is already occupied")
		user_inp(board)
	else:
		board[user_x-1][user_y-1]=opponent

def display_board(board):
	print("-------------------")
	for i in range(3):
		for j in range(3):
			if board[i][j]==no_move:
				print("|     ",end="")
			else:
				print('| ',board[i][j],' ',end="")

		print("|")
	print("-------------------")
player="x"
opponent="o"
no_move="_"
is_play=True
while is_play:
	board=[
			[no_move, no_move, no_move],
			[no_move, no_move, no_move],
			[no_move, no_move, no_move]
		  ]


	is_player_move=False
	cnt=0
	flag=True
	while flag:
		if is_player_move:
			player111 = findBestMove(board)
			if player111.x==-1:
				flag=False
				break
			is_player_move=False
			board[player111.x][player111.y]=player
			display_board(board)
			score=evaluate(board)
			if score!=0:
				print("YOU LOSE")
				break
		else:
			print("Enter your move")
			user_inp(board)

			is_player_move=True
			display_board(board)
			score=evaluate(board)
			if score!=0:
				print("YOU WIN")
				break
	if score==0:
		print("DRAW")
	print("You want to play again( Y (yes) / N (no) ) ")
	if input().lower()!="y":
		is_play=False

