



f = open("C:\\Users\\PC\\Python Education\\Python New\\day12\\seagames.inp", "r")
N = int(f.readline())    
athletes = {}

for i in range (N):
    name = f.readline().strip()
    medals = f. readline().strip()
    athletes[name] = medals
    
f.close()
points = {}

for name, medals in athletes.items():
    point = 0
    for medal in medals:
        if medal == "G":
            point += 3
        elif medal == "S":
            point += 2
        elif medal == "B":
            point += 1
    points[name] = point

sorted_list = sorted(points.items(), key=lambda x: x[1], reverse= True)
max_gold = 0
gold_list = []

for name, medals in athletes.items():
    gold = medals.count("G")
    if gold > max_gold:
        max_gold = gold
        gold_list = [name]
    elif gold == max_gold:
        gold_list.append(name)
    
oanh_list = []

for name in athletes.keys():
    if name.split()[-1] == "Oanh":
        oanh_list.append(name)
gold_athletes = []
for name, medals in athletes.items():
    if "G" in medals: gold_athletes.append(name)
f = open("C:\\Users\\PC\\Python Education\\Python New\\day12\\seagames.out" , "w")

for i in range(3):
    name, point = sorted_list[i]
    f.write(f"{name}{medals}\n")
    
f.write(f"{len(oanh_list)}\n")

f.close()



























































