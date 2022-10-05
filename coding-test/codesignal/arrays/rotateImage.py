def solution(a):
    # List comprehension of
    # for i in range(length):
    #     for j in range(length):
    #         a[-j-1][i]

    length = len(a)
    return  [
                [
                    a[-j-1][i] 
                    for j in range(length)
                ] 
                for i in range(length)
            ]
