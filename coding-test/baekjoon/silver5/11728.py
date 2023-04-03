# [11728] 배열 합치기
# https://www.acmicpc.net/problem/11728
import sys
NM = sys.stdin.readline()
print(" ".join(sorted(sys.stdin.read().split(), key=int)))