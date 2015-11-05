import os
from collections import defaultdict as ddict

# Generated by https://github.com/coventry/cl-zip-codes
datapath = os.path.dirname(__file__)
path = os.path.join(datapath, 'more-cl-zipcodes.txt')

zipcl = {}
for line in open(path):
    region, z = line.split()
    zipcl[z] = region

clzip = ddict(list)
for zip, region in zipcl.items():
    clzip[region].append(zip)

conus_states = set(l.split()[-1] for l in open(os.path.join(datapath, 'states.txt')))
zipstate = dict(l.split() for l in open(os.path.join(datapath, 'zipstate.txt')))

def conus_p(z):
    return zipstate[z] in conus_states
