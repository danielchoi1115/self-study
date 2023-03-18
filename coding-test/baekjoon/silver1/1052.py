# https://www.acmicpc.net/problem/1052

import sys
N, K = map(int,sys.stdin.readline().split())


# 그리디 알고리즘 사용

powers = [pow(2, i) for i in range(30)]
for i in range(K):
    # 만약 N이 2의 배수라면 물병을 살 필요 없음
    if N in powers:
        N = 0
        break
    
    for p in range(len(powers)):
        # N에 가장 가까운 2의 배수를 찾은 수 뺀다.
        # K 한 개 소모
        # 마지막 루프에는 남은 N을 2의 배수로 만들기 위한 물병 수를 계산한다.
        if powers[p] > N:
            if i == K-1:
                N = powers[p] - N
            else:
                N -= powers[p-1]
            break
        
print(N)
