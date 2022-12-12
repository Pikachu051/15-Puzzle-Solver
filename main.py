import webbrowser
import numpy as np

def MAIN_FUNCTION(puzzle):
    """INPUT"""
    # puzzle = np.array([[int(input()) for _ in range(4)], [int(input()) for _ in range(4)], [int(input()) for _ in range(4)], [int(input()) for _ in range(4)]])
    # print("INPUT")
    # print(puzzle)
    """POSITION"""
    for x in range(0, 4):
        for y in range(0, 4):
            if puzzle[x][y] == 1:
                posi_1_row = x
                posi_1_colum = y
            elif puzzle[x][y] == 2:
                posi_2_row = x
                posi_2_colum = y
            elif puzzle[x][y] == 3:
                posi_3_row = x
                posi_3_colum = y
            elif puzzle[x][y] == 4:
                posi_4_row = x
                posi_4_colum = y
            elif puzzle[x][y] == 5:
                posi_5_row = x
                posi_5_colum = y
            elif puzzle[x][y] == 6:
                posi_6_row = x
                posi_6_colum = y
            elif puzzle[x][y] == 7:
                posi_7_row = x
                posi_7_colum = y
            elif puzzle[x][y] == 8:
                posi_8_row = x
                posi_8_colum = y
            elif puzzle[x][y] == 9:
                posi_9_row = x
                posi_9_colum = y
            elif puzzle[x][y] == 10:
                posi_10_row = x
                posi_10_colum = y
            elif puzzle[x][y] == 11:
                posi_11_row = x
                posi_11_colum = y
            elif puzzle[x][y] == 12:
                posi_12_row = x
                posi_12_colum = y
            elif puzzle[x][y] == 13:
                posi_13_row = x
                posi_13_colum = y
            elif puzzle[x][y] == 14:
                posi_14_row = x
                posi_14_colum = y
            elif puzzle[x][y] == 15:
                posi_15_row = x
                posi_15_colum = y
            # else:
            #     posi_0_row = x
            #     posi_0_colum = y

    """MANHATTAN"""
    man_1 = abs(posi_1_row-0)+abs(posi_1_colum-0)
    man_2 = abs(posi_2_row-0)+abs(posi_2_colum-1)
    man_3 = abs(posi_3_row-0)+abs(posi_3_colum-2)
    man_4 = abs(posi_4_row-0)+abs(posi_4_colum-3)
    man_5 = abs(posi_5_row-1)+abs(posi_5_colum-0)
    man_6 = abs(posi_6_row-1)+abs(posi_6_colum-1)
    man_7 = abs(posi_7_row-1)+abs(posi_7_colum-2)
    man_8 = abs(posi_8_row-1)+abs(posi_8_colum-3)
    man_9 = abs(posi_9_row-2)+abs(posi_9_colum-0)
    man_10 = abs(posi_10_row-2)+abs(posi_10_colum-1)
    man_11 = abs(posi_11_row-2)+abs(posi_11_colum-2)
    man_12 = abs(posi_12_row-2)+abs(posi_12_colum-3)
    man_13 = abs(posi_13_row-3)+abs(posi_13_colum-0)
    man_14 = abs(posi_14_row-3)+abs(posi_14_colum-1)
    man_15 = abs(posi_15_row-3)+abs(posi_15_colum-2)
    # man_0 = abs(posi_0_row-3)+abs(posi_0_colum-3)
    total_man = man_1+man_2+man_3+man_4+man_5+man_6+man_7+man_8+man_9+man_10+man_11+man_12+man_13+man_14+man_15
    return total_man
MAIN_FUNCTION(np.array([[int(input()) for _ in range(4)], [int(input()) for _ in range(4)], \
    [int(input()) for _ in range(4)], [int(input()) for _ in range(4)]]))

def Pararell12(check1, check2, count):
    """Pararell"""
    if count % 2 == 0:
        check1 -= 1
        return check1, check2
    elif count % 2 == 1:
        check2 -= 1
        return check1, check2
def Pararell123(check1, check2, check3, count):
    """Pararell"""
    # num_1 = 0
    # num_2 = 0
    # num_3 = 0
    # if num_1 >= 2 and num_2 >= 2:
    #     check3 -=
    #     return check1, check2, check3
    # elif num_1 >= 2 and num_3 >= 2:
    #     check2 -= 1
    #     return check1, check2, check3
    # elif num_2 >= 2 and num_3 >= 2:
    #     check1 -= 1
    #     return check1, check2, check3
    if count % 3 == 0:
        num_1 += 1
        check1 -= 1
        return check1, check2, check3
    elif count % 3 == 1:
        num_1 += 1
        check2 -= 1
        return check1, check2, check3
    elif count % 3 == 2:
        num_1 += 1
        check3 -= 1
        return check1, check2, check3
def Pararell123(check1, check2, check3, check4, count):
    """Pararell"""
    if count % 4 == 0:
        check1 -= 1
        return check1, check2, check3, check4
    elif count % 4 == 1:
        check2 -= 1
        return check1, check2, check3, check4
    elif count % 4 == 2:
        check3 -= 1
        return check1, check2, check3, check4
    elif count % 4 == 3:
        check4 -= 1
        return check1, check2, check3, check4
