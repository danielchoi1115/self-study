# https://www.tutorialsteacher.com/python/string-translate

mystr = 'Tutorials Teacher'
trans_dict = {'T':'1','o':'2','l':'3','h':'4'}
mytable = mystr.maketrans(trans_dict)
mystr_translated = mystr.translate(mytable)

print('Original String:', mystr)
print('Translated String:', mystr_translated)
print('Table:', mytable)