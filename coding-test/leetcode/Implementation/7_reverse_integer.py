class Solution:
    def reverse(self, x: int) -> int:
        MAX = pow(2, 31)-1
        MIN = -pow(2, 31)
        new_x = int(str(x)[::-1]) if x > 0 else -1 * (int(str(x*-1)[::-1]))
        return 0 if x == 0 or new_x > MAX or new_x < MIN else new_x 