import pytest
from chess_puzzle import *


def test_location2index1():
    assert location2index("e2") == (5,2)
def test_location2index2():
    assert location2index("a1") == (1,1)
def test_location2index3():
    assert location2index("b3") == (2,3)
def test_location2index4():
    assert location2index("c4") == (3,4)
def test_location2index5():
    assert location2index("z5") == (26,5)
def test_location2index6():
    assert location2index("w18") == (23,18)

def test_index2location1():
    assert index2location(5,2) == "e2"
def test_index2location2():
    assert index2location(1,6) == "a6"
def test_index2location3():
    assert index2location(25,1) == "y1"
def test_index2location4():
    assert index2location(3,15) == "c15"
def test_index2location5():
    assert index2location(7,10) == "g10"
def test_index2location6():
    assert index2location(15,20) == "o20"

wq1 = Queen(4,4,True)
wk1 = King(3,5,True)
wq2 = Queen(3,1,True)

bq1 = Queen(5,3,False)
bk1 = King(2,3,False)


B1 = (5, [wq1, wk1, wq2, bq1, bk1])

"""
  ♔  
   ♕ 
 ♚  ♛
     
  ♕  
"""

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False
def test_is_piece_at2():
    assert is_piece_at(4,4, B1) == True
def test_is_piece_at3():
    assert is_piece_at(3,5, B1) == True
def test_is_piece_at4():
    assert is_piece_at(3,4, B1) == False
def test_is_piece_at5():
    assert is_piece_at(1,1, B1) == False
def test_is_piece_at6():
    assert is_piece_at(7,1, B1) == False

def test_piece_at1():
    assert piece_at(3,1, B1) == wq2
def test_piece_at2():
    assert piece_at(2,3, B1) == bk1
def test_piece_at3():
    assert piece_at(5,3, B1) == bq1
def test_piece_at4():
    assert piece_at(3,5, B1) == wk1
def test_piece_at5():
    assert piece_at(4,4, B1) == wq1

def test_can_reach1():
    #test Queen
    assert wq1.can_reach(5,4, B1) == True
def test_can_reach2():
    assert wq1.can_reach(5,3, B1) == True
def test_can_reach3():
    assert wq1.can_reach(6,6, B1) == False
def test_can_reach4():
    assert wq1.can_reach(3,5, B1) == False
def test_can_reach5():
    assert wq1.can_reach(3,2, B1) == False
def test_can_reach11():
    assert bq1.can_reach(3,5, B1) == False
def test_can_reach6():
    #test King
    assert bk1.can_reach(2,5, B1) == False
def test_can_reach7():
    assert bk1.can_reach(1,4, B1) == True
def test_can_reach8():
    assert bk1.can_reach(3,3, B1) == True
def test_can_reach9():
    assert wk1.can_reach(4,4, B1) == False
def test_can_reach10():
    assert wk1.can_reach(3,6, B1) == False

def test_can_move_to1():
    #test Queen
    assert wq1.can_move_to(5,4, B1) == False
def test_can_move_to2():
    assert wq1.can_move_to(5,3, B1) == True
def test_can_move_to3():
    assert bq1.can_move_to(3,5, B1) == False
def test_can_move_to4():
    assert bq1.can_move_to(3,1, B1) == True
def test_can_move_to5():
    assert bq1.can_move_to(2,3, B1) == False
def test_can_move_to11():
    wq1a = Queen(5,3, True)
    wq2a = Queen(5,1, True)
    wk1a = King(2,3,True)
    bk1a = King(1,5,False)
    B2 = (5, [wq1a, wq2a, wk1a, bk1a])
    assert wq2a.can_move_to(1,5, B2) == True
def test_can_move_to6():
    #test King
    assert wk1.can_move_to(2,4, B1) == False
def test_can_move_to7():
    assert wk1.can_move_to(2,5, B1) == True
def test_can_move_to8():
    assert wk1.can_move_to(3,4, B1) == False
def test_can_move_to9():
    assert bk1.can_move_to(2,2, B1) == False
def test_can_move_to10():
    assert bk1.can_move_to(1,4, B1) == False

def test_move_to1():
    wk1a = King(4,5, True)
    Actual_B = wk1.move_to(4,5, B1)
    Expected_B = (5, [wq1, wk1a, wq2, bq1, bk1])
    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5
    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_move_to2():
    bq1a = Queen(4,4, False)
    Actual_B = bq1.move_to(4,4, B1)
    Expected_B = (5, [wk1, wq2, bq1a, bk1])
    assert Actual_B[0] == 5
    for piece1 in Actual_B[1]: 
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece in Expected_B[1]: 
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_move_to3():
    bk1a = King(2,2, False)
    Actual_B = bk1.move_to(2,2, B1)
    Expected_B = (5, [wq1, wk1, wq2, bq1, bk1a])
    assert Actual_B[0] == 5
    for piece1 in Actual_B[1]: 
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece in Expected_B[1]: 
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_move_to4():
    wq1a = Queen(5,3, True)
    Actual_B = wq1.move_to(5,3, B1)
    Expected_B = (5, [wq1a, wk1, wq2, bk1])
    assert Actual_B[0] == 5
    for piece1 in Actual_B[1]: 
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece in Expected_B[1]: 
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_move_to5():
    wq2a = Queen(5,1, True)
    Actual_B = wq2.move_to(5,1, B1)
    Expected_B = (5, [wq1, wk1, wq2a, bq1, bk1])
    assert Actual_B[0] == 5
    for piece1 in Actual_B[1]: 
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece in Expected_B[1]: 
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
   
def test_is_check1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_check(True, B2) == True
def test_is_check2():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_check(True, B1) == False
def test_is_check3():
    bk1a = King(2,2, False)
    B2 = (5, [wk1, wq1, wq2, bq1, bk1a])
    assert is_check(False, B2) == True   
def test_is_check4():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_check(False, B1) == False
def test_is_check5():
    B2 = (5, [wk1, bq1, bk1])
    assert is_check(True, B2) == True
def test_is_check6():
    wk1a = King(4,5, True)
    bq1a = Queen(4,4, False)
    B2 = (5, [wk1a, bq1a, wq2, bq1, bk1])
    assert is_check(True, B2) == True
    
def test_is_checkmate1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_checkmate(True, B2) == False
def test_is_checkmate2():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_checkmate(False, B2) == False
def test_is_checkmate3():
    bk1b = King(3,4,False)
    wk1b = King(3,2,True)
    wq1b = Queen(1,4,True)
    B2 = (4, [bk1b, wk1b, wq1b])
    assert is_checkmate(False, B2) == True
def test_is_checkmate4():
    bk1b = King(3,4,False)
    bq1b = Queen(1,2,False)
    wk1b = King(3,2,True)
    wq1b = Queen(1,4,True)
    B2 = (4, [bk1b, bq1b, wk1b, wq1b])
    assert is_checkmate(False, B2) == False
def test_is_checkmate5():
    bk1b = King(3,4,False)
    bq1b = Queen(1,2,False)
    wk1b = King(3,2,True)
    wq1b = Queen(1,4,True)
    B2 = (4, [bk1b, bq1b, wk1b, wq1b])
    assert is_checkmate(True, B2) == False

def test_is_stalemate1():
    assert is_stalemate(True, B1) == False
def test_is_stalemate2():
    assert is_stalemate(False, B1) == False
def test_is_stalemate3():
    bk1b = King(3,4,False)
    bq1b = Queen(1,2,False)
    wk1b = King(3,2,True)
    wq1b = Queen(1,4,True)
    B2 = (4, [bk1b, bq1b, wk1b, wq1b])
    assert is_stalemate(False, B1) == False
def test_is_stalemate4():
    bk1b = King(3,4,False)
    bq1b = Queen(1,2,False)
    wk1b = King(3,2,True)
    wq1b = Queen(1,4,True)
    B2 = (4, [bk1b, bq1b, wk1b, wq1b])
    assert is_stalemate(True, B1) == False
def test_is_stalemate5():
    bk1c = King(3,2,False)
    wk1c = King(1,4,True)
    wq1c = Queen(1,1,True)
    wq2c = Queen(4,4,True)
    B3 = (4, [bk1c, wk1c, wq1c, wq2c])
    assert is_stalemate(False, B3) == True

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_read_board2():
    B = read_board("board_examp2.txt")
    wk1d = King(3,4,True)
    B4 = (5, [wq1, wk1d, wq2, bq1, bk1])
    assert B[0] == 5
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B4[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece1 in B4[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_read_board3():
    B = read_board("board_examp3.txt")
    B5 = (5, [wq1, wk1, bq1, bk1])
    assert B[0] == 5
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B5[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece1 in B5[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found       
def test_read_board4():
    B = read_board("board_examp4.txt")
    B6 = (5, [wq1, wk1, wq2, bk1])
    assert B[0] == 5
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B6[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece1 in B6[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_read_board5():
    B = read_board("board_examp5.txt")
    bq1c = Queen(5,2,False)
    B7 = (5, [wq1, wk1, wq2, bq1c, bk1])
    assert B[0] == 5
    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B7[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
    for piece1 in B7[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_conf2unicode1():
    assert conf2unicode(B1).rstrip("\n") == "  ♔  \n   ♕ \n ♚  ♛\n     \n  ♕  "
def test_conf2unicode2():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert conf2unicode(B2).rstrip("\n") == "  ♔  \n     \n ♚  ♛\n     \n  ♕  "
def test_conf2unicode3():
    bk1c = King(3,2,False)
    wk1c = King(1,4,True)
    wq1c = Queen(1,1,True)
    wq2c = Queen(4,4,True)
    B3 = (4, [bk1c, wk1c, wq1c, wq2c])
    assert conf2unicode(B3).rstrip("\n") == "♔  ♕\n    \n  ♚ \n♕   "
def test_conf2unicode4():
    wk1d = King(3,4,True)
    B4 = (5, [wq1, wk1d, wq2, bq1, bk1])
    assert conf2unicode(B4).rstrip("\n") == "     \n  ♔♕ \n ♚  ♛\n     \n  ♕  "
def test_conf2unicode5():
    B5 = (5, [wq1, wk1, bq1, bk1])
    assert conf2unicode(B5).rstrip("\n") == "  ♔  \n   ♕ \n ♚  ♛\n     \n     "