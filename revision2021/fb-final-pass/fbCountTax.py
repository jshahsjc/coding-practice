"""
[2:58 PM, 11/14/2019] Shrinidhi: You are given a list of triples
[2:58 PM, 11/14/2019] Shrinidhi: Tuples*
[2:58 PM, 11/14/2019] Shrinidhi: Which contains the salary slabs
[2:58 PM, 11/14/2019] Shrinidhi: And the tax percentage
[2:58 PM, 11/14/2019] Shrinidhi: Calculate the tax based on input salary
[3:00 PM, 11/14/2019] Shrinidhi: Say you are given [(10000,0.1),(25000,0.3),(40000,0.4),(None,0.5)]
[3:01 PM, 11/14/2019] Shrinidhi: If say salary is 90000
Then the tax will be:
10000*0.1 + 25000*0.3 + 40000*0.4 + 15000*0.5
[3:02 PM, 11/14/2019] Shrinidhi: ++++
Calculate the tax
"""

def countTax(salary, slabs):
    untaxed = salary
    taxed = 0
    tax = 0

    if salary < slabs[0][0]:
        return 0

    for slab in slabs:
        if slab[0] is not None and untaxed > 0:
            slab_amt = min((slab[0] - taxed), untaxed)
            taxed += slab_amt
            untaxed -= slab_amt
            tax += slab_amt * slab[1]

        if slab[0] is None and untaxed > 0:
            slab_amt = untaxed
            taxed += slab_amt
            untaxed -= slab_amt
            tax += slab_amt * slab[1]

        if untaxed == 0:
            break


    return tax
