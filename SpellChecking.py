n = int(input())
d = set()
txt = set()
for i in range(n):
    word = input()
    d.update([word.lower()])
k = int(input())
for j in range(k):
    phrase = input()
    phrase = phrase.lower().split(' ')
    txt.update(*[phrase])
print(*(txt - d))
