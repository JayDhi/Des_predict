import csv
import pickle
from itertools import combinations

def get_valid(line):
    trip = []
    for p in line:
        if p == '':
            return trip
        trip.append(p)

def create_comb(line):
    l = len(line)
    index = list(range(0, l-2))
    des = (l-1, l)
    comb = [(i*2, i*2+1) for i in range(0, int(len(index)/2))]
    combs = list(combinations(comb, int(len(index)/2)-1))
    combs_lists = []
    for comb_ in combs:
        combs_list = []
        for c in comb_:
            combs_list.append(line[c[0]])
            combs_list.append(line[c[1]])
        combs_lists.append(combs_list)
    return combs_lists

f = csv.reader(open("c:/Users/james/Desktop/trips.csv", "r"))
outf = open("c:/Users/james/Desktop/trips.pkl", "wb")
trips = [get_valid(line) for line in f]
prefix = []
for t in trips:
    try:
        prefix.append(create_comb(t))
    except:
        continue
pickle.dump(prefix, outf)
outf.close()
