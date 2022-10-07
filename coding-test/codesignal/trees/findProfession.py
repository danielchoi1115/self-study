import math
def solution(level, pos):
    track = []
    for i in range(level, 0, -1):
        track.append((pos, pos % 2 == 1))
        pos = math.ceil(pos/2)
    
    # let 'E' be True
    # and 'D' be False
    orig = True
    for pos, isFirst in reversed(track):
        if not isFirst:
            orig = not orig
    return 'Engineer' if orig else 'Doctor'
    
    
# 200% smarter solution by jedrick
def solution(level, pos):
    """
    Level 1: E
    Level 2: ED
    Level 3: EDDE
    Level 4: EDDEDEED
    Level 5: EDDEDEEDDEEDEDDE 
    1
    10
    1001
    10010110
    1001011001101001
    Level input is not necessary because first elements are the same
    The result is based on the count of 1's in binary representation of position-1
    If position is even, then Engineer; Else Doctor
    """
    bits  = bin(pos-1).count('1')
    if bits%2 == 0: 
        return "Engineer"
    else:
        return "Doctor"
print(bin(10-1).count('1'))

    
    