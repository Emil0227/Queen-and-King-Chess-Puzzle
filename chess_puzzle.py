def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    col = ord(loc[0]) - ord('a') + 1
    row = int(loc[1:])
    return (col,row)
	
def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    col = chr(x + ord('a') - 1)
    row = str(y)
    combinedStr = col + row
    return combinedStr

class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        pos_x = pos_X
        pos_y = pos_Y
        pos_y = pos_Y
        side = side_

Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B''' 
    for eachPiece in B[1]:
        if (eachPiece.pos_x == pos_X) and (eachPiece.pos_y == pos_Y):
            return True
    return False
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for eachPiece in B[1]:
        if (eachPiece.pos_x == pos_X) and (eachPiece.pos_y == pos_Y):
            return eachPiece

class Queen(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.pos_y = pos_Y
        self.side = side_
	
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this queen can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''
        from_col = self.pos_x
        from_row = self.pos_y
        to_col = pos_X
        to_row = pos_Y
        startPointCol = min(from_col,to_col)
        finPointCol = max(from_col,to_col)
        startPointRow = min(from_row,to_row)
        finPointRow = max(from_row,to_row)
        if (pos_X > B[0]) or (pos_Y > B[0]): 
            return False
        elif is_piece_at(to_col, to_row, B) and piece_at(to_col, to_row, B).side == self.side: 
            return False
        elif from_col == to_col:
            for y in range (startPointRow+1,finPointRow):
                if is_piece_at(from_col, y, B):
                    return False  
        elif from_row == to_row: 
            for x in range (startPointCol+1,finPointCol):
                if is_piece_at(from_row, x, B):
                    return False
        elif abs(to_col - from_col) == abs(to_row - from_row): 
            for y in range (startPointRow+1,finPointRow):
                startPointCol += 1
                if is_piece_at(startPointCol, y, B):
                    return False  
        else:
            return False
        return True  
    
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this queen can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        
        Hints:
        - firstly, check [Rule1] and [Rule3] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule4], use is_check on new board
        '''
        import copy
        tempB = copy.deepcopy(B)
        if self.can_reach(pos_X, pos_Y, B)==False:
            return False
        elif is_piece_at(pos_X, pos_Y, B): 
            tempList = tempB[1]
            for i in range (len(tempList)):
                if (tempList[i].pos_x == pos_X and tempList[i].pos_y == pos_Y):
                    tempB[1].pop(i)
                    break
        for p1 in tempB[1]:
            if (p1.pos_x == self.pos_x and p1.pos_y == self.pos_y):
                p1.pos_x = pos_X
                p1.pos_y = pos_Y   
        if is_check(self.side, tempB):
            return False
        return True
    
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this queen to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        import copy
        tempB = copy.deepcopy(B)
        if is_piece_at(pos_X, pos_Y, B): 
            tempB = (B[0],copy.deepcopy(B[1]))
            tempList = tempB[1]
            for i in range (len(tempList)):
                if (tempList[i].pos_x == pos_X and tempList[i].pos_y == pos_Y):
                    tempB[1].pop(i)
                    break
        for p1 in tempB[1]:
            if (p1.pos_x == self.pos_x and p1.pos_y == self.pos_y):
                p1.pos_x = pos_X
                p1.pos_y = pos_Y 
        return tempB


class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.pos_y = pos_Y
        self.side = side_
        
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''
        from_col = self.pos_x
        from_row = self.pos_y
        to_col = pos_X
        to_row = pos_Y
        if (pos_X > B[0]) or (pos_Y > B[0]): 
            return False
        elif is_piece_at(to_col, to_row, B) and piece_at(to_col, to_row, B).side == self.side: 
            return False
        elif (from_col == to_col) and (abs(to_row - from_row) ==1): 
            return True
        elif (from_row == to_row) and (abs(to_col - from_col) ==1): 
            return True
        elif abs(to_col - from_col) == 1 and abs(to_row - from_row) == 1: 
            return True
        else:
            return False
        
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        import copy
        tempB = copy.deepcopy(B)
        if self.can_reach(pos_X, pos_Y, B)==False:
            return False
        elif is_piece_at(pos_X, pos_Y, B): 
            tempList = tempB[1]
            for i in range (len(tempList)):
                if (tempList[i].pos_x == pos_X and tempList[i].pos_y == pos_Y):
                    tempB[1].pop(i)
                    break
        for p1 in tempB[1]:
            if (p1.pos_x == self.pos_x and p1.pos_y == self.pos_y):
                p1.pos_x = pos_X
                p1.pos_y = pos_Y   
        if is_check(self.side, tempB):
            return False
        return True
    
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        import copy
        tempB = copy.deepcopy(B)
        if is_piece_at(pos_X, pos_Y, B): 
            tempB = (B[0],copy.deepcopy(B[1]))
            tempList = tempB[1]
            for i in range (len(tempList)):
                if (tempList[i].pos_x == pos_X and tempList[i].pos_y == pos_Y):
                    tempB[1].pop(i)
                    break
        for p1 in tempB[1]:
            if (p1.pos_x == self.pos_x and p1.pos_y == self.pos_y):
                p1.pos_x = pos_X
                p1.pos_y = pos_Y 
        return tempB

def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    for p in B[1]:
        if isinstance(p,King) and (side == p.side):
            kingPiece = p;
    for p1 in B[1]:
        if p1.can_reach(kingPiece.pos_x, kingPiece.pos_y, B):
            return True
    return False

def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_move_to
    '''
    if is_check(side, B):
        for p in B[1]:
            if p.side == side:
                for x in range (1,B[0]+1):
                    for y in range (1,B[0]+1):
                        if p.can_move_to(x, y, B):
                            return False
        return True
    return False    

def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints: 
    - use is_check
    - use can_move_to 
    '''
    if is_check(side, B)==False:
        for p in B[1]:
            if p.side == side:
                for x in range (1,B[0]+1):
                    for y in range (1,B[0]+1):
                        if p.can_move_to(x, y, B):
                            return False
        return True
    return False  

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    num : int
    pieceList:list = []
    infile = open (filename,"r")
    num = int(infile.readline())
    if num<1 or num>26: 
        raise IOError("This is not a valid file. File name for initial configuration: ")            
    lineCount = 0
    nextLine = infile.readline()
    while nextLine != "":
        numK = 0
        side : bool
        lineCount += 1
        if lineCount == 1:
            side = True
        elif lineCount == 2:
            side = False
        segmentList: list[str] = nextLine.split(",") 
        for segment in segmentList: 
            startFrom = 0
            while True:
                if startFrom >= len(segment):
                    raise IOError("This is not a valid file. File name for initial configuration: ")
                elif segment[startFrom] != " ":
                    break
                startFrom += 1
            meaningfulSegment = segment[startFrom:] 
            loc = meaningfulSegment[1:]
            coor: tuple[int, int] = location2index(loc)
            if coor[0]>num or coor[1]>num:
                raise IOError("This is not a valid file. File name for initial configuration: ")
            else:
                if meaningfulSegment[0] == "K":
                    numK += 1;
                    p = King(coor[0],coor[1],side)
                elif meaningfulSegment[0] == "Q":
                    p = Queen(coor[0],coor[1],side)
                else:
                    raise IOError("This is not a valid file. File name for initial configuration: ")
            pieceList.append(p)
        if numK > 1:
            raise IOError("This is not a valid file. File name for initial configuration: ")
        nextLine = infile.readline()  
    import copy
    for i in range (len(pieceList)):
        tempList = copy.deepcopy(pieceList)
        tempPiece = tempList[i]
        tempList.pop(i)
        for p in tempList:
            if p.pos_x == tempPiece.pos_x and p.pos_y == tempPiece.pos_y:
                raise IOError("This is not a valid file. File name for initial configuration: ")      
    infile.close()
    return (num, pieceList)        

def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    outfile = open (filename,"w")
    outfile.write(str(B[0])+"\n")
    whitePieces:list = []
    blackPieces:list = []
    for p in B[1]:
        if p.side == True:
            if isinstance(p,King):
                loc = "K"+ index2location(p.pos_x, p.pos_y)
            else:
                loc = "Q"+ index2location(p.pos_x, p.pos_y)
            whitePieces.append(loc)
        else:
            if isinstance(p,King):
                loc = "K"+ index2location(p.pos_x, p.pos_y)
            else:
                loc = "Q"+ index2location(p.pos_x, p.pos_y)
            blackPieces.append(loc)
    str1 = " , ".join (whitePieces)
    str2 = " , ".join (blackPieces)
    outfile.write(str1+"\n")
    outfile.write(str2)
    outfile.close()

def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''
    import random
    isTraversing = True
    while isTraversing:
        x = random.randint(1,B[0])
        y = random.randint(1,B[0])
        pieceList = B[1]
        for p in pieceList:
            if p.side == False: #Find each black piece
                if p.can_move_to(x, y, B):
                    return (p, x, y)
                    isTraversing = False

def conf2unicode(B: Board) -> str: 
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    num = B[0]
    row = num
    col = 1
    line  = []
    while row >= 1:
        for col in range (1,num+1):
            if is_piece_at(col, row, B):
                p = piece_at(col, row, B)
                if isinstance(p,Queen):
                    if p.side == True:
                        line.append("\u2655")#white queen
                    else:
                        line.append("\u265B")#black queen
                else:
                    if p.side == True:
                        line.append("\u2654")#white king
                    else:
                        line.append("\u265A")#black king
            else:
                line.append("\u2001")
        line.append("\n")
        row -= 1
    return "".join(line)

def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''   
    #Initiation
    isFileCorrect = False
    print("File name for initial configuration: ")
    while isFileCorrect == False:
        initialInput = input( )
        if initialInput == "QUIT":
            quit()
        else:
            try:
                Board = read_board(initialInput)
            except IOError:
                print(IOError)
            else:
                print (conf2unicode(Board)) 
                isFileCorrect = True
    
    #Play rounds
    isGameOver = False
    print ("Next move of White: ")
    while isGameOver == False:
        whiteMove = input()
        flag : int
        if whiteMove == "QUIT":
            outputFile = input ("File name to store the configuration: ")
            save_board(outputFile, Board)
            print ("The game configuration saved.")
            quit()
        else:
            for i in range (1,len(whiteMove)):
                if whiteMove[i].isalpha():#second alpha occurs
                    flag = i
                    break
        startLoc = whiteMove[0:flag]
        endLoc = whiteMove[flag:]
        startIndex = location2index(startLoc)
        endIndex = location2index(endLoc)
        p = piece_at(startIndex[0], startIndex[1], Board)
        if p.can_move_to(endIndex[0], endIndex[1], Board):
            Board = p.move_to(endIndex[0], endIndex[1], Board)
            print ("The configuration after White's move is: ")
            print (conf2unicode(Board)) 
            if is_checkmate(False, Board):#checkmate for Black
                print("Game over. White wins.")
                quit()
            elif is_stalemate(False, Board):#stalemate for Black
                print("Game over. Stalemate.")
                quit()
            else:#culculate black move
                blackMove: tuple[Piece, int, int] = find_black_move(Board)
                startLocBlack : str = index2location(blackMove[0].pos_x, blackMove[0].pos_y)
                endLocBlack : str = index2location(blackMove[1], blackMove[2])
                Board = blackMove[0].move_to(blackMove[1], blackMove[2], Board)
                s = startLocBlack+endLocBlack
                print ("Next move of Black is "+ s + ". The configuration after Black's move is:")
                print (conf2unicode(Board))
                if is_checkmate(True, Board):#checkmate for White
                    print("Game over. Black wins.")
                    quit()
                elif is_stalemate(True, Board):#stalemate for White
                    print("Game over. Stalemate.")
                    quit()
                else:
                    print ("Next move of White:")
        else:
            print("This is not a valid move. Next move of White:")   

if __name__ == '__main__': #keep this in
   main()
