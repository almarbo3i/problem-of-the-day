
def maximumHight(black, white):
    hight = 0
    ballsInRow = 1
    total = black + white
    WhiteUse = True
    
    while total >= ballsInRow:
        if WhiteUse and white >= ballsInRow:
            white = white - ballsInRow
            
        elif not WhiteUse and black >= ballsInRow:
            black = black - ballsInRow
            
        else:
            break
        
        hight = hight + 1
        total = total - ballsInRow
        ballsInRow = ballsInRow + 1
        WhiteUse = not WhiteUse
    
    return hight
print("input-> 2 balls black and 4 white. output->:  ", maximumHight(2,4))
print("input-> 2 balls black and 1 white. output->:  ", maximumHight(2,1))
print("input-> 1 balls black and 1 white. output->:  ", maximumHight(1,1))
print("input-> 10 balls black and 1 white. output->: ", maximumHight(10,1))
        
    



