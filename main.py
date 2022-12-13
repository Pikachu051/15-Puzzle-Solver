import webbrowser
import numpy as np

def MAIN_FUNCTION(puzzle):
    """INPUT"""
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
def main():
    """mainfunction"""
    sample_puzzle = np.array([[1, 2, 3, 4] , [5, 6 , 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    sample_puzzle = np.reshape(sample_puzzle,(4,4))
    puzzle_new = np.array([[int(input()) for _ in range(4)], [int(input()) for _ in range(4)], [int(input()) for _ in range(4)], [int(input()) for _ in range(4)]])
    print(puzzle_new)
    manhat = MAIN_FUNCTION(puzzle_new)
    print(manhat)
    check_1 = []
    check_2 = []
    check_3 = []
    check_4 = []
    check_5 = []
    check_6 = []
    check_7 = []
    check_8 = []
    check_9 = []
    check_10 = []
    check_11 = []
    check_12 = []
    check_13 = []
    check_14 = []
    check_15 = []
    check_16 = []
    check_17 = []
    check_18 = []
    check_19 = []
    check_20 = []
    check_21 = []
    check_22 = []
    check_23 = []
    check_24 = []
    check_9_2 = []
    check_10_2 = []
    check_11_2 = []
    check_12_2 = []
    check_13_2 = []
    check_14_2 = []
    check_15_2 = []
    check_16_2 = []
    check_17_2 = []
    check_18_2 = []
    check_19_2= []
    check_20_2 = []
    check_21_2 = []
    check_22_2 = []
    check_23_2 = []
    check_24_2 = []
    check_21_3 = []
    check_22_3 = []
    check_23_3 = []
    check_24_3 = []
    check_21_4 = []
    check_22_4 = []
    check_23_4 = []
    check_24_4 = []
    for _ in range(0, 999):
        manhat = MAIN_FUNCTION(puzzle_new)
        if manhat == 0:
            break
        elif manhat > 0:
            for x in range(0, 4):
                if manhat == 0:
                     break
               for y in range(0, 4):
                    if puzzle_new[x][y] == 0 and x == 0 and y == 0:
                        check_1 = np.array([])
                        check_1 = np.append( check_1, puzzle_new)
                        check_1 = np.reshape(check_1,(4,4))
                        check_1[x][y] = check_1[x+1][y]
                        check_1[x+1][y] = 0
                        manhat_check_1 = MAIN_FUNCTION(check_1)
                        check_2 = np.array([])
                        check_2 = np.append(check_2, puzzle_new)
                        check_2 = np.reshape(check_2,(4,4))
                        check_2[x][y] = check_2[x][y+1]
                        check_2[x][y+1] = 0
                        manhat_check_2 = MAIN_FUNCTION(check_2)
                        if manhat_check_1_2 == manhat_check_1:
                            puzzle_new = check_1
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_1_2 == manhat_check_2:
                            puzzle_new = check_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 0 and y == 3:
                        check_3 = np.array([])
                        check_3 = np.append(check_3, puzzle_new)
                        check_3 = np.reshape(check_3,(4,4))
                        check_3[x][y] = check_3[x+1][y]
                        check_3[x+1][y] = 0
                        manhat_check_3 = MAIN_FUNCTION(check_3)
                        check_4 = np.array([])
                        check_4 = np.append(check_4, puzzle_new)
                        check_4 = np.reshape(check_4,(4,4))
                        check_4[x][y] = check_4[x][y-1]
                        check_4[x][y-1] = 0
                        manhat_check_4 = MAIN_FUNCTION(check_4)
                        manhat_check_3_4 = min(manhat_check_3, manhat_check_4)
                        if manhat_check_3_4 == manhat_check_3:
                            puzzle_new = check_3
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_3_4 == manhat_check_4:
                            puzzle_new = check_4
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 3 and y == 0:
                        check_5 = np.array([])
                        check_5 = np.append(check_5, puzzle_new)
                        check_5 = np.reshape(check_5,(4,4))
                        check_5[x][y] = check_5[x-1][y]
                        check_5[x-1][y] = 0
                        manhat_check_5 = MAIN_FUNCTION(check_5)
                        check_6 = np.array([])
                        check_6 = np.append(check_6, puzzle_new)
                        check_6 = np.reshape(check_6,(4,4))
                        check_6[x][y] = check_6[x][y+1]
                        check_6[x][y+1] = 0
                        manhat_check_6 = MAIN_FUNCTION(check_6)
                        manhat_check_5_6 = min(manhat_check_5, manhat_check_6)
                        if manhat_check_5_6 == manhat_check_5:
                            puzzle_new = check_5
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_5_6 == manhat_check_6:
                            puzzle_new = check_6
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 3 and y == 3:
                        check_7 = np.array([])
                        check_7 = np.append(check_7, puzzle_new)
                        check_7 = np.reshape(check_7,(4,4))
                        check_7[x][y] = check_7[x-1][y]
                        check_7[x-1][y] = 0
                        manhat_check_7 = MAIN_FUNCTION(check_7)
                        check_8 = np.array([])
                        check_8 = np.append(check_8, puzzle_new)
                        check_8 = np.reshape(check_8,(4,4))
                        check_8[x][y] = check_8[x][y-1]
                        check_8[x][y-1] = 0
                        manhat_check_8 = MAIN_FUNCTION(check_8)
                        manhat_check_7_8 = min(manhat_check_7, manhat_check_8)
                        if manhat_check_7_8 == manhat_check_7:
                            puzzle_new = check_7
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_7_8 == manhat_check_8:
                            puzzle_new = check_8
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 0 and y == 1:
                        check_9 = np.array([])
                        check_9 = np.append(check_9, puzzle_new)
                        check_9 = np.reshape(check_9,(4,4))
                        check_9[x][y] = check_9[x+1][y]
                        check_9[x+1][y] = 0
                        manhat_check_9 = MAIN_FUNCTION(check_9)
                        check_10 = np.array([])
                        check_10 = np.append(check_10, puzzle_new)
                        check_10 = np.reshape(check_10,(4,4))
                        check_10[x][y] = check_10[x][y-1]
                        check_10[x][y-1] = 0
                        manhat_check_10 = MAIN_FUNCTION(check_10)
                        check_11 = np.array([])
                        check_11 = np.append(check_11, puzzle_new)
                        check_11 = np.reshape(check_11,(4,4))
                        check_11[x][y] = check_11[x][y+1]
                        check_11[x][y+1] = 0
                        manhat_check_11 = MAIN_FUNCTION(check_11)
                        manhat_check_9_10_11 = min(manhat_check_9, manhat_check_10, manhat_check_11)
                        if manhat_check_9_10_11 == manhat_check_9:
                            puzzle_new = check_9
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_9_10_11 == manhat_check_10:
                            puzzle_new = check_10
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_9_10_11 == manhat_check_11:
                            puzzle_new = check_11
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 0 and y == 2:
                        check_9_2 = np.array([])
                        check_9_2 = np.append(check_9_2, puzzle_new)
                        check_9_2 = np.reshape(check_9_2,(4,4))
                        check_9_2[x][y] = check_9_2[x+1][y]
                        check_9_2[x+1][y] = 0
                        manhat_check_9_2 = MAIN_FUNCTION(check_9_2)
                        check_10_2 = np.array([])
                        check_10_2 = np.append(check_10_2, puzzle_new)
                        check_10_2 = np.reshape(check_10_2,(4,4))
                        check_10_2[x][y] = check_10_2[x][y-1]
                        check_10_2[x][y-1] = 0
                        manhat_check_10_2 = MAIN_FUNCTION(check_10_2)
                        check_11_2 = np.array([])
                        check_11_2 = np.append(check_11_2, puzzle_new)
                        check_11_2 = np.reshape(check_11_2,(4,4))
                        check_11_2[x][y] = check_11_2[x][y+1]
                        check_11_2[x][y+1] = 0
                        manhat_check_11_2 = MAIN_FUNCTION(check_11_2)
                        manhat_check_9_2_10_11 = min(manhat_check_9_2, manhat_check_10_2, manhat_check_11_2)
                        if manhat_check_9_2_10_11 == manhat_check_9_2:
                            puzzle_new = check_9_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_9_2_10_11 == manhat_check_10_2:
                            puzzle_new = check_10_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_9_2_10_11 == manhat_check_11_2:
                            puzzle_new = check_11_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 3 and y == 1:
                        check_12 = np.array([])
                        check_12 = np.append(check_12, puzzle_new)
                        check_12 = np.reshape(check_12,(4,4))
                        check_12[x][y] = check_12[x-1][y]
                        check_12[x-1][y] = 0
                        manhat_check_12 = MAIN_FUNCTION(check_12)
                        check_13 = np.array([])
                        check_13 = np.append(check_13, puzzle_new)
                        check_13 = np.reshape(check_13,(4,4))
                        check_13[x][y] = check_13[x][y-1]
                        check_13[x][y-1] = 0
                        manhat_check_13 = MAIN_FUNCTION(check_13)
                        check_14 = np.array([])
                        check_14 = np.append(check_14, puzzle_new)
                        check_14 = np.reshape(check_14,(4,4))
                        check_14[x][y] = check_14[x][y+1]
                        check_14[x][y+1] = 0
                        manhat_check_14 = MAIN_FUNCTION(check_14)
                        manhat_check_12_13_14 = min(manhat_check_12, manhat_check_13, manhat_check_14)
                        if manhat_check_12_13_14 == manhat_check_12:
                            puzzle_new = check_12
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_12_13_14 == manhat_check_13:
                            puzzle_new = check_13
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_12_13_14 == manhat_check_14:
                            puzzle_new = check_14
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 3 and y == 2:
                        check_12_2 = np.array([])
                        check_12_2 = np.append(check_12_2, puzzle_new)
                        check_12_2 = np.reshape(check_12_2,(4,4))
                        check_12_2[x][y] = check_12_2[x-1][y]
                        check_12_2[x-1][y] = 0
                        manhat_check_12_2 = MAIN_FUNCTION(check_12_2)
                        check_13_2 = np.array([])
                        check_13_2 = np.append(check_13_2, puzzle_new)
                        check_13_2 = np.reshape(check_13_2,(4,4))
                        check_13_2[x][y] = check_13_2[x][y-1]
                        check_13_2[x][y-1] = 0
                        manhat_check_13_2 = MAIN_FUNCTION(check_13_2)
                        check_14_2 = np.array([])
                        check_14_2 = np.append(check_14_2, puzzle_new)
                        check_14_2 = np.reshape(check_14_2,(4,4))
                        check_14_2[x][y] = check_14_2[x][y+1]
                        check_14_2[x][y+1] = 0
                        manhat_check_14_2 = MAIN_FUNCTION(check_14_2)
                        manhat_check_12_2_13_14 = min(manhat_check_12_2, manhat_check_13_2, manhat_check_14_2)
                        if manhat_check_12_2_13_14 == manhat_check_12_2:
                            puzzle_new = check_12_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_12_2_13_14 == manhat_check_13_2:
                            puzzle_new = check_13_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_12_2_13_14 == manhat_check_14_2:
                            puzzle_new = check_14_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 1 and y == 0:
                        check_15 = np.array([])
                        check_15 = np.append(check_15, puzzle_new)
                        check_15 = np.reshape(check_15,(4,4))
                        check_15[x][y] = check_15[x+1][y]
                        check_15[x+1][y] = 0
                        manhat_check_15 = MAIN_FUNCTION(check_15)
                        check_16 = np.array([])
                        check_16 = np.append(check_16, puzzle_new)
                        check_16 = np.reshape(check_16,(4,4))
                        check_16[x][y] = check_16[x-1][y]
                        check_16[x-1][y] = 0
                        manhat_check_16 = MAIN_FUNCTION(check_16)
                        check_17 = np.array([])
                        check_17 = np.append(check_17, puzzle_new)
                        check_17 = np.reshape(check_17,(4,4))
                        check_17[x][y] = check_17[x][y+1]
                        check_17[x][y+1] = 0
                        manhat_check_17 = MAIN_FUNCTION(check_17)
                        manhat_check_15_16_17 = min(manhat_check_15, manhat_check_16, manhat_check_17)
                        if manhat_check_15_16_17 == manhat_check_15:
                            puzzle_new = check_15
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_15_16_17 == manhat_check_16:
                            puzzle_new = check_16
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_15_16_17 == manhat_check_17:
                            puzzle_new = check_17
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 2 and y == 0:
                        check_15_2 = np.array([])
                        check_15_2 = np.append(check_15_2, puzzle_new)
                        check_15_2 = np.reshape(check_15_2,(4,4))
                        check_15_2[x][y] = check_15_2[x+1][y]
                        check_15_2[x+1][y] = 0
                        manhat_check_15_2 = MAIN_FUNCTION(check_15_2)
                        check_16_2 = np.array([])
                        check_16_2 = np.append(check_16_2, puzzle_new)
                        check_16_2 = np.reshape(check_16_2,(4,4))
                        check_16_2[x][y] = check_16_2[x-1][y]
                        check_16_2[x-1][y] = 0
                        manhat_check_16_2 = MAIN_FUNCTION(check_16_2)
                        check_17_2 = np.array([])
                        check_17_2 = np.append(check_17_2, puzzle_new)
                        check_17_2 = np.reshape(check_17_2,(4,4))
                        check_17_2[x][y] = check_17_2[x][y+1]
                        check_17_2[x][y+1] = 0
                        manhat_check_17_2 = MAIN_FUNCTION(check_17_2)
                        manhat_check_15_2_16_17 = min(manhat_check_15_2, manhat_check_16_2, manhat_check_17_2)
                        if manhat_check_15_2_16_17 == manhat_check_15_2:
                            puzzle_new = check_15_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_15_2_16_17 == manhat_check_16_2:
                            puzzle_new = check_16_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_15_2_16_17 == manhat_check_17_2:
                            puzzle_new = check_17_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 1 and y == 3:
                        check_18 = np.array([])
                        check_18 = np.append(check_18, puzzle_new)
                        check_18 = np.reshape(check_18,(4,4))
                        check_18[x][y] = check_18[x+1][y]
                        check_18[x+1][y] = 0
                        manhat_check_18 = MAIN_FUNCTION(check_18)
                        check_19 = np.array([])
                        check_19 = np.append(check_19, puzzle_new)
                        check_19 = np.reshape(check_19,(4,4))
                        check_19[x][y] = check_19[x-1][y]
                        check_19[x-1][y] = 0
                        manhat_check_19 = MAIN_FUNCTION(check_19)
                        check_20 = np.array([])
                        check_20 = np.append(check_20, puzzle_new)
                        check_20 = np.reshape(check_20,(4,4))
                        check_20[x][y] = check_20[x][y-1]
                        check_20[x][y-1] = 0
                        manhat_check_20 = MAIN_FUNCTION(check_20)
                        manhat_check_18_19_20 = min(manhat_check_18, manhat_check_19, manhat_check_20)
                        if manhat_check_18_19_20 == manhat_check_18:
                            puzzle_new = check_18
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_18_19_20 == manhat_check_19:
                            puzzle_new = check_19
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_18_19_20 == manhat_check_20:
                            puzzle_new = check_20
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 2 and y == 3:
                        check_18_2 = np.array([])
                        check_18_2 = np.append(check_18_2, puzzle_new)
                        check_18_2 = np.reshape(check_18_2,(4,4))
                        check_18_2[x][y] = check_18_2[x+1][y]
                        check_18_2[x+1][y] = 0
                        manhat_check_18_2 = MAIN_FUNCTION(check_18_2)
                        check_19_2 = np.array([])
                        check_19_2 = np.append(check_19_2, puzzle_new)
                        check_19_2 = np.reshape(check_19_2,(4,4))
                        check_19_2[x][y] = check_19_2[x-1][y]
                        check_19_2[x-1][y] = 0
                        manhat_check_19_2 = MAIN_FUNCTION(check_19_2)
                        check_20_2 = np.array([])
                        check_20_2 = np.append(check_20_2, puzzle_new)
                        check_20_2 = np.reshape(check_20_2,(4,4))
                        check_20_2[x][y] = check_20_2[x][y-1]
                        check_20_2[x][y-1] = 0
                        manhat_check_20_2 = MAIN_FUNCTION(check_20_2)
                        manhat_check_18_2_19_20 = min(manhat_check_18_2, manhat_check_19_2, manhat_check_20_2)
                        if manhat_check_18_2_19_20 == manhat_check_18_2:
                            puzzle_new = check_18_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_18_2_19_20 == manhat_check_19_2:
                            puzzle_new = check_19_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 1 and y == 1:
                        check_21 = np.array([])
                        check_21 = np.append(check_21, puzzle_new)
                        check_21 = np.reshape(check_21,(4,4))
                        check_21[x][y] = check_21[x-1][y]
                        check_21[x-1][y] = 0
                        manhat_check_21 = MAIN_FUNCTION(check_21)
                        check_22 = np.array([])
                        check_22 = np.append(check_22, puzzle_new)
                        check_22 = np.reshape(check_22,(4,4))
                        check_22[x][y] = check_22[x+1][y]
                        check_22[x+1][y] = 0
                        manhat_check_22 = MAIN_FUNCTION(check_22)
                        check_23 = np.array([])
                        check_23 = np.append(check_23, puzzle_new)
                        check_23 = np.reshape(check_23,(4,4))
                        check_23[x][y] = check_23[x][y-1]
                        check_23[x][y-1] = 0
                        manhat_check_23 = MAIN_FUNCTION(check_23)
                        check_24 = np.array([])
                        check_24 = np.append(check_24, puzzle_new)
                        check_24 = np.reshape(check_24,(4,4))
                        check_24[x][y] = check_24[x][y+1]
                        check_24[x][y+1] = 0
                        manhat_check_24 = MAIN_FUNCTION(check_24)
                        manhat_check_21_22_23_24 = min(manhat_check_21, manhat_check_22, manhat_check_23, manhat_check_24)
                        if manhat_check_21_22_23_24 == manhat_check_21:
                            puzzle_new = check_21
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_22_23_24 == manhat_check_22:
                            puzzle_new = check_22
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_22_23_24 == manhat_check_23:
                            puzzle_new = check_23
                            print(puzzle_new)
                            if manhat == 0:
                                break
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                        elif manhat_check_21_22_23_24 == manhat_check_24:
                            puzzle_new = check_24
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 1 and y == 2:
                        check_21_2 = np.array([])
                        check_21_2 = np.append(check_21_2, puzzle_new)
                        check_21_2 = np.reshape(check_21_2,(4,4))
                        check_21_2[x][y] = check_21_2[x-1][y]
                        check_21_2[x-1][y] = 0
                        manhat_check_21_2 = MAIN_FUNCTION(check_21_2)
                        check_22_2 = np.array([])
                        check_22_2 = np.append(check_22_2, puzzle_new)
                        check_22_2 = np.reshape(check_22_2,(4,4))
                        check_22_2[x][y] = check_22_2[x+1][y]
                        check_22_2[x+1][y] = 0
                        manhat_check_22_2 = MAIN_FUNCTION(check_22_2)
                        check_23_2 = np.array([])
                        check_23_2 = np.append(check_23_2, puzzle_new)
                        check_23_2 = np.reshape(check_23_2,(4,4))
                        check_23_2[x][y] = check_23_2[x][y-1]
                        check_23_2[x][y-1] = 0
                        manhat_check_23_2 = MAIN_FUNCTION(check_23_2)
                        check_24_2 = np.array([])
                        check_24_2 = np.append(check_24_2, puzzle_new)
                        check_24_2 = np.reshape(check_24_2,(4,4))
                        check_24_2[x][y] = check_24_2[x][y+1]
                        check_24_2[x][y+1] = 0
                        manhat_check_24_2 = MAIN_FUNCTION(check_24_2)
                        manhat_check_21_2_22_23_24 = min(manhat_check_21_2, manhat_check_22_2, manhat_check_23_2, manhat_check_24_2)
                        if manhat_check_21_2_22_23_24 == manhat_check_21_2:
                            puzzle_new = check_21_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_2_22_23_24 == manhat_check_22_2:
                            puzzle_new = check_22_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_2_22_23_24 == manhat_check_23_2:
                            puzzle_new = check_23_2
                            print(puzzle_new)
                            if manhat == 0:
                                break
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                        elif manhat_check_21_2_22_23_24 == manhat_check_24_2:
                            puzzle_new = check_24_2
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 2 and y == 1:
                        check_21_3 = np.array([])
                        check_21_3 = np.append(check_21_3, puzzle_new)
                        check_21_3 = np.reshape(check_21_3,(4,4))
                        check_21_3[x][y] = check_21_3[x-1][y]
                        check_21_3[x-1][y] = 0
                        manhat_check_21_3 = MAIN_FUNCTION(check_21_3)
                        check_22_3 = np.array([])
                        check_22_3 = np.append(check_22_3, puzzle_new)
                        check_22_3 = np.reshape(check_22_3,(4,4))
                        check_22_3[x][y] = check_22_3[x+1][y]
                        check_22_3[x+1][y] = 0
                        manhat_check_22_3 = MAIN_FUNCTION(check_22_3)
                        check_23_3 = np.array([])
                        check_23_3 = np.append(check_23_3, puzzle_new)
                        check_23_3 = np.reshape(check_23_3,(4,4))
                        check_23_3[x][y] = check_23_3[x][y-1]
                        check_23_3[x][y-1] = 0
                        manhat_check_23_3 = MAIN_FUNCTION(check_23_3)
                        check_24_3 = np.array([])
                        check_24_3 = np.append(check_24_3, puzzle_new)
                        check_24_3 = np.reshape(check_24_3,(4,4))
                        check_24_3[x][y] = check_24_3[x][y+1]
                        check_24_3[x][y+1] = 0
                        manhat_check_24_3 = MAIN_FUNCTION(check_24_3)
                        manhat_check_21_3_22_23_24 = min(manhat_check_21_3, manhat_check_22_3, manhat_check_23_3, manhat_check_24_3)
                        if manhat_check_21_3_22_23_24 == manhat_check_21_3:
                            puzzle_new = check_21_3
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_3_22_23_24 == manhat_check_22_3:
                            puzzle_new = check_22_3
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_3_22_23_24 == manhat_check_23_3:
                            puzzle_new = check_23_3
                            print(puzzle_new)
                            if manhat == 0:
                                break
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                        elif manhat_check_21_3_22_23_24 == manhat_check_24_3:
                            puzzle_new = check_24_3
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                    elif puzzle_new[x][y] == 0 and x == 2 and y == 2:
                        check_21_4 = np.array([])
                        check_21_4 = np.append(check_21_4, puzzle_new)
                        check_21_4 = np.reshape(check_21_4,(4,4))
                        check_21_4[x][y] = check_21_4[x-1][y]
                        check_21_4[x-1][y] = 0
                        manhat_check_21_4 = MAIN_FUNCTION(check_21_4)
                        check_22_4 = np.array([])
                        check_22_4 = np.append(check_22_4, puzzle_new)
                        check_22_4 = np.reshape(check_22_4,(4,4))
                        check_22_4[x][y] = check_22_4[x+1][y]
                        check_22_4[x+1][y] = 0
                        manhat_check_22_4 = MAIN_FUNCTION(check_22_4)
                        check_23_4 = np.array([])
                        check_23_4 = np.append(check_23_4, puzzle_new)
                        check_23_4 = np.reshape(check_23_4,(4,4))
                        check_23_4[x][y] = check_23_4[x][y-1]
                        check_23_4[x][y-1] = 0
                        manhat_check_23_4 = MAIN_FUNCTION(check_23_4)
                        check_24_4 = np.array([])
                        check_24_4 = np.append(check_24_4, puzzle_new)
                        check_24_4 = np.reshape(check_24_4,(4,4))
                        check_24_4[x][y] = check_24_4[x][y+1]
                        check_24_4[x][y+1] = 0
                        manhat_check_24_4 = MAIN_FUNCTION(check_24_4)
                        manhat_check_21_4_22_23_24 = min(manhat_check_21_4, manhat_check_22_4, manhat_check_23_4, manhat_check_24_4)
                        if manhat_check_21_4_22_23_24 == manhat_check_21_4:
                            puzzle_new = check_21_4
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_4_22_23_24 == manhat_check_22_4:
                            puzzle_new = check_22_4
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
                        elif manhat_check_21_4_22_23_24 == manhat_check_23_4:
                            puzzle_new = check_23_4
                            print(puzzle_new)
                            if manhat == 0:
                                break
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                        elif manhat_check_21_4_22_23_24 == manhat_check_24_4:
                            puzzle_new = check_24_4
                            print(puzzle_new)
                            manhat = MAIN_FUNCTION(puzzle_new)
                            print(manhat)
                            if manhat == 0:
                                break
    if (puzzle_new == sample_puzzle).all():
        print("Finished! Problem solved.")
    else:
        print("Error: Can't find the valid solution. The problem is too complicated for this program.")
main()
