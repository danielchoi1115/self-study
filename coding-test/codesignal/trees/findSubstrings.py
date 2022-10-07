def solution(words, parts):
    # Create Trie
    trie = {}
    for p in parts:
        pt = trie
        for c in p:
            if c not in pt:
                pt[c] = {}
            pt = pt[c]
        pt['-'] = p
    print(trie)
    # check if substring exist
    def getSubstring(word):
        pt = trie
        substring = ''
        for c in word:
            if c in pt:
                if '-' in pt:
                    substring = pt['-']
                pt = pt[c]
            else:
                break
            if '-' in pt:
                substring = pt['-']
        return substring
    
    # 
    res = []
    for idx, word in enumerate(words):
        substring = ''
        pos = -1
        for i in range(len(word)):
            sub = getSubstring(word[i:])
            if sub and len(sub) > len(substring):
                substring = sub
                pos = i
        
        if substring: 
            res.append(f"{word[:pos]}[{substring}]{word[pos+len(substring):]}")
        else:
            res.append(word)
            
    return res

words=["Apple", 
 "Melon", 
 "Orange", 
 "Watermelon"]
parts=["a", 
 "mel", 
 "lon", 
 "el", 
 "An"]
print(solution(words, parts))