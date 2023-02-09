from collections import Counter
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        # same letters
        # different letters

        sameDict = {}
        diffDict = {}
        length = 0
        for word in words:
            # if repeated letter is in sameSet, then add 4 to length
            # for ex, aa and aa can be added symmetrically.
            if word[0] == word[1]:
                if word in sameDict and sameDict[word] > 0:
                    length += 4
                    sameDict[word] -= 1
                else:
                    sameDict[word] = sameDict.setdefault(word, 0) + 1
                continue

            reverse = word[::-1]
            if reverse in diffDict and diffDict[reverse] > 0:
                length += 4
                diffDict[reverse] -= 1
            else: 
                diffDict[word] = diffDict.setdefault(word, 0) + 1

        if sum(sameDict.values()) > 0: length += 2

        return length

# Faster Answer
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        counter = Counter(words)
        put_in_center = False

        for word in counter:
            if word[0] == word[1]:
                if counter[word] % 2 == 0:
                    ans += counter[word]
                else:
                    ans += counter[word] - 1
                    put_in_center = True
            elif word[0] < word[1]:
                if word[::-1] in counter:
                    ans += 2 * min(counter[word], counter[word[::-1]])
        
        if put_in_center:
            ans += 1        
        return ans * 2
    
s = Solution()
a = s.longestPalindrome(["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"])
print(a)