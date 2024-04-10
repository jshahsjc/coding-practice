"""
Asked in FB coding screen

You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal

"""

import csv
from collections import defaultdict
from math import sqrt

def dinoBySpeed(dataset1, dataset2):
    dinos = defaultdict(dict)

    with open(dataset2) as f2:
        ds2 = csv.reader(f2) ## list of lists
        for d in ds2:
            if d[-1] == 'bipedal':
                dinos[d[0]]['stride'] = float(d[1])
    with open(dataset1) as f1:
        ds1 = csv.reader(f1) ## list of lists
        for d in ds1:
            if d[0] in dinos:
                dinos[d[0]]['leg'] = float(d[1])

    for d in dinos:
        dinos[d]['speed'] = (d['stride']/d['leg'] - 1) * sqrt(leg * 9.8)
    for d in sorted(dinos.items(), key=lambda x: x[1]['speed'], reverse=True):
        print(d[0])
