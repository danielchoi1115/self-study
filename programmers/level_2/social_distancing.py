# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    for room in places:
        if checkRoom(room):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def checkRoom(room):
    for rowIdx, row in enumerate(room):
        for colIdx, col in enumerate(row):
            if col != 'P':
                continue
            if not validateSocialDistancing(rowIdx, colIdx, room):
                return 0
    return 1


def manhattanDistance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)


def validateSocialDistancing(rowIdx, colIdx, room):
    # 각 자리의 거리두기 조사
    for targetRow in range(5):
        for targetCol in range(5):
            # 자기 자신은 패스
            if targetRow == rowIdx and targetCol == colIdx:
                continue

            # 맨해튼거리가 2 초과면 패스
            distance = manhattanDistance(rowIdx, colIdx, targetRow, targetCol)
            if distance > 2:
                continue

            # P가 아니면 패스
            t = room[targetRow][targetCol]
            if room[targetRow][targetCol] != 'P':
                continue

            # 바로 옆자리가 P일경우 false 리턴
            if distance == 1:
                return False

            # 직선거리 2칸 자리 검사
            if targetRow == rowIdx or targetCol == colIdx:
                # 가운데 자리가 X가 아니면 false
                if room[int((targetRow+rowIdx)/2)][int((targetCol+colIdx)/2)] != 'X':
                    return False
            else:
                # 대각선 자리 검사
                if room[rowIdx][targetCol] != 'X' or room[targetRow][colIdx] != 'X':
                    return False

    return True
