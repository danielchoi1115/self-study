from collections import Counter
from time import time

# player counter
# ranked distinct를 각 각 정렬
# O(N + M) time
# instead of using nested loop, I used only one loop to traverse the rankings.
# It will loop over the ranking scores and find out if player score can be placed in the current index.


def climbingLeaderboard(ranked, player):
    rankings = []
    # sort ranked list in ascending order
    ranked_distinct = sorted(set(ranked))
    # length of ranked array
    n = len(ranked_distinct)
    # dummy value when traversing
    ranked_distinct.append(-1)

    # player scores will be appended as many as its occurrence
    player_count = Counter(player)
    # get player scores in ascending order
    player_distinct = sorted(player_count.keys())

    # first score to look for
    current_score = player_distinct.pop(0)
    for idx, rank in enumerate(ranked_distinct):
        # if the player's score is less than the ranking
        if rank > current_score:
            # get indices of every score that are less than the current ranking index
            while current_score < rank and current_score > -1:
                rankings.extend([n - idx + 1] * player_count[current_score])
                current_score = player_distinct.pop(0) if player_distinct else -1
        elif idx == n:
            # else if player's score is greater than the entire ranking
            while current_score >= rank and current_score > -1:
                # get all indices of every score that are greater than the highest ranking
                rankings.extend([1] * player_count[current_score])
                current_score = player_distinct.pop(0) if player_distinct else -1
    return rankings


# ranked = list(range(20000000))
ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 95]  # * 10000 + [25] * 4000 + [50] * 8000

ranked = list(map(int, "295 294 291 287 287 285 285 284 283 279 277 274 274 271 270 268 268 268 264 260 259 258 257 255 252 250 244 241 240 237 236 236 231 227 227 227 226 225 224 223 216 212 200 197 196 194 193 189 188 187 183 182 178 177 173 171 169 165 143 140 137 135 133 130 130 130 128 127 122 120 116 114 113 109 106 103 99 92 85 81 69 68 63 63 63 61 57 51 47 46 38 30 28 25 22 15 14 12 6 4".split()))
player = list(map(int, "5 5 6 14 19 20 23 25 29 29 30 30 32 37 38 38 38 41 41 44 45 45 47 59 59 62 63 65 67 69 70 72 72 76 79 82 83 90 91 92 93 98 98 100 100 102 103 105 106 107 109 112 115 118 118 121 122 122 123 125 125 125 127 128 131 131 133 134 139 140 141 143 144 144 144 144 147 150 152 155 156 160 164 164 165 165 166 168 169 170 171 172 173 174 174 180 184 187 187 188 194 197 197 197 198 201 202 202 207 208 211 212 212 214 217 219 219 220 220 223 225 227 228 229 229 233 235 235 236 242 242 245 246 252 253 253 257 257 260 261 266 266 268 269 271 271 275 276 281 282 283 284 285 287 289 289 295 296 298 300 300 301 304 306 308 309 310 316 318 318 324 326 329 329 329 330 330 332 337 337 341 341 349 351 351 354 356 357 366 369 377 379 380 382 391 391 394 396 396 400".split()))

t1 = time()
print(climbingLeaderboard(ranked, player))
print(round(time() - t1, 3))
