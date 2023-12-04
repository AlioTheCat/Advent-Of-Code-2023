with open("Day One.txt", "r") as dayone :
    t = dayone.readlines()
print(t)

dg = "0123456789"
dgs = {"one" : 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
dgts = list(dg) + [i for i in dgs]

"""
for char in expt :
    t = [i.replace(char, str(dgs[char])) for i in t]

for char in dgs :
    t = [i.replace(char, str(dgs[char])) for i in t]"""

digits = []

for line in t :
    dg_list = []
    start = 0
    for i in range(len(line)) :
        for x in dgts :
            if x in line[start:i+1] and (len(dg_list)==0 or x!=dg_list[-1]) :
                start = i
                dg_list.append(x)
    digits.append(dg_list)
print(digits)
integers = [[int(j) if j in dg else dgs[j] for j in u] for u in digits]
wanteds = [10*i[0]+i[-1] for i in integers]
"""
indexes = [sorted([(i.index(p[0]), p) for p in dgts if p in i], key = lambda u,v : u) for i in t]
digits = [[int(j[1]) if j[1] in dg else dgs[j[1]] for j in u] for u in indexes]
wanteds = [10*i[0]+i[-1] for i in digits]
"""
#[(0, '6'), (1, '7'), (2, '9'), (3, '8'), (4, 'seven')

