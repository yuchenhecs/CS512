fname = 'phrase_YELP.emb'
fname2 = 'phrase_YELP.txt'

with open(fname) as f:
    lines = f.readlines()

output = open(fname2, 'w')

for l in lines:
    tokens = l.split()
    if len(tokens) <= 0 or tokens[0][0] != '_' or len(tokens[0])<=1:
        continue
    output.write(l)

output.close()