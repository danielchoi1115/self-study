# 19532 수학은 비대면강의입니다
# https://www.acmicpc.net/problem/19532
import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())
print((c*e-f*b)//(a*e-d*b), (f*a-c*d)//(a*e-b*d))