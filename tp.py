word = open('file.txt')
d = dict()

for lin in word:
    lin = lin.strip()
    wds = lin.split()
    for w in wds:
        d[w] = d.get(w, 0) + 1

tmp = list()
for k, v in d.items():
    new = (v, k)
    tmp.append(new)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5]:
    print(k, v)

# largest = -1
# the_word = None
# for k, v in d.items():
#     print(k, v)
#     if v > largest:
#         largest = v
#         the_word = k
#
# print("Done", the_word, largest)

s = {5, 6}
s*3