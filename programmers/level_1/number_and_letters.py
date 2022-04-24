# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

literal_to_num = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def solution(s):
    answer = 0
    s = str(s)
    for literal, num in literal_to_num.items():
        s = s.replace(literal, num)
    answer = int(s)
    return answer
