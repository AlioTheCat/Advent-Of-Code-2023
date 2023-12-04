t = open("Day Four.txt").readlines()
t = [t[i].replace("\n", "").split(": ")[1] for i in range(len(t))]

games = [[[int(nb) for nb in i.split(" ") if nb!=''] for i in u.split(" | ")] for u in t]


def points(game) :
    winning, picked = game.copy()
    score = -1
    for i in winning :
        if i in picked :
            score+=1
    return 0 if score<0 else 2**score

print(sum([points(i) for i in games]))

def get_cards(n) : # n = numéro de la game, indexé àpd 1
    winning, picked = games[n-1].copy()
    matching = 0
    for i in winning :
        if i in picked :
            matching+=1
    return range(n+1,n+1+matching)

N = len(games)
pending = {i:1 for i in range(1,len(games)+1)} ; cardtotal = 0 ; curr = 1
print(pending)
while pending[N] :
    cardtotal+=1
    if pending[curr]>0 :
        pending[curr]-=1
    else :
        curr+=1
        pending[curr]-=1
        print(f"{curr}/{N} de faits", cardtotal)
    cards = get_cards(curr)
    for i in cards :
        pending[i]+=1

print(cardtotal)