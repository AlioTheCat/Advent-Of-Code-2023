t = [line.replace("\n", "") for line in open("Day Three.txt").readlines()] #C'est plus simple d'enlever les linebreaks pour le traitement

def locate_numbers(t):
    locations = []
    for line in range(len(t)) :
        for i in range(len(t[line])) :
            if t[line][i] in "0123456789" :
                if len(locations)>0 and locations[-1][-1]==i :
                    locations[-1][-1]=i+1
                else :
                    locations.append([line, i, i+1])
    return locations

locations = locate_numbers(t)
line_locations = [[(beg,end) for line, beg, end in locations if line==i] for i in range(len(t))] #Pas efficace mais menfou

def digit_adjacency(line, ind) : #input : location
    border_left = [(line-1, ind-1), (line, ind-1), (line+1, ind-1)] #Rmq : toutes les lignes ont la même taille, pratique.
    border_right = [(line-1, ind+1), (line, ind+1), (line+1, ind+1)]
    upper_bound = [(line-1,ind)]
    lower_bound = [(line+1,ind)]
    return [(y,x) for y, x in border_left+border_right+upper_bound+lower_bound if y in range(len(t)) and x in range(len(t[0])) and t[y][x] in "0123456789"]

def locate_gears(t):
    gears = []
    for line in range(len(t)) :
        for i in range(len(t[line])) :
            if t[line][i]=='*' :
                if len(digit_adjacency(line, i))>=2 :
                    gears.append(digit_adjacency(line, i))
    return gears

def gear_factor(gear) : #Attention : il peut y avoir un seul nombre dans un gear suspecté pour l'instant ! Il faut vérifier qu'il y en a bien deux.
    numbs = []
    for line, x in gear :
        for beg, end in line_locations[line] :
            if x in range(beg,end) and int(t[line][beg:end]) not in numbs :
                numbs.append(int(t[line][beg:end]))
    if len(numbs)>=3 :
        print("OULALALALALALA PULL UP")
    if len(numbs)== 2 :
        print(numbs, numbs[0]*numbs[1])
    return 0 if len(numbs)<2 else numbs[0]*numbs[1]
            


total_gear_factor = sum([gear_factor(g) for g in locate_gears(t)])




def is_adjacent(line, beg, end) : #input : location
    is_special = lambda line, i : t[line][i] not in "0123456789."
    border_left = [(line-1, beg-1), (line, beg-1), (line+1, beg-1)] #Rmq : toutes les lignes ont la même taille, pratique.
    border_right = [(line-1, end), (line, end), (line+1, end)]
    upper_bound = [(line-1,x) for x in range(beg,end)]
    lower_bound = [(line+1,x) for x in range(beg,end)]
    #print(t[line][beg:end], [t[y][x] for y, x in border_left+border_right+upper_bound+lower_bound if y in range(len(t)) and x in range(len(t[0]))])
    return any([is_special(y,x) for y, x in border_left+border_right+upper_bound+lower_bound if y in range(len(t)) and x in range(len(t[0]))])




parts = [int(t[line][beg:end]) for line, beg, end in locate_numbers(t) if is_adjacent(line, beg, end)]
print(sum(parts))