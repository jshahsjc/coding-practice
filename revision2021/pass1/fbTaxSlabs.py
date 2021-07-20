"""
[2:58 PM, 11/14/2019] Shrinidhi: You are given a list of triples
[2:58 PM, 11/14/2019] Shrinidhi: Tuples*
[2:58 PM, 11/14/2019] Shrinidhi: Which contains the salary slabs
[2:58 PM, 11/14/2019] Shrinidhi: And the salary percentage
[2:58 PM, 11/14/2019] Shrinidhi: Calculate the tax based on input salary
[3:00 PM, 11/14/2019] Shrinidhi: Say you are given [(10000,0.1),(25000,0.3),(40000,0.4),(None,0.5)]
[3:01 PM, 11/14/2019] Shrinidhi: If say salary is 90000
Then the tax will be:
10000*0.1 + 25000*0.3 + 40000*0.4 + 15000*0.5
[3:02 PM, 11/14/2019] Shrinidhi: ++++
Calculate the tax
"""
from collections import defaultdict

def findTax(salary, slabs):
#    keep = defaultdict()
    taxed = 0
    non_taxed = salary
    total_tax = 0
    # while non_taxed >= 0:
    for slab in slabs:
        # count tax paid per slab until either the last default 'Null' slab is hit
        # or the non taxed amount is more than zero
        if slab[0] != None and non_taxed > 0:
            slab_amt = min((slab[0] - taxed), non_taxed)
        #    keep[slab[0]] = slab_amt * slab[1]
            total_tax += (slab_amt * slab[1])
            taxed += slab_amt
            non_taxed = salary - taxed
        # if we have hit the last slab 'Null',
        # tax the remaining non_taxed money at the default rate
        if slab[0] == None and non_taxed > 0:
            slab_amt = non_taxed
        #    keep[slab[0]] = slab_amt * slab[1]
            total_tax += (slab_amt * slab[1])
            taxed += slab_amt
            non_taxed = salary - taxed
        # if there is no taxable salary left, break
        if non_taxed == 0:
            break

    return total_tax

slabs =  [(10000,0.1),(25000,0.3),(40000,0.4),(None,0.5)]
print(findTax(90000, slabs))
