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

from collections import defaultdict
from math import sqrt
import csv

def getBipedals(dataset1, dataset2):
    dinos = defaultdict(dict)
    with open(dataset2) as f:
        csvF2 = csv.reader(f)
        for line in csvF2[1:]:
            if line[2] == 'bipedal':
                dinos[line[0]]["STRIDE_LENGTH"] = float(line[1])
    with open(dataset1) as f:
        csvF1 = csv.reader(f)
        if "LEG_LENGTH" in csvF[0]:
            legIndx = csvF[0].index("LEG_LENGTH")
        for line in csfF1[1:]:
            if line[0] in dinos:
                dinos[line[0]]["LEG_LENGTH"] = float(line[legIndx])
    for dino in dinos:
        dino["SPEED"] = ((dino["STRIDE_LENGTH"]/dino["LEG_LENGTH"]) - 1) * sqrt(dino["LEG_LENGTH"] * 9.8)

    for dino, attr in sorted(dinos.items(), key = lambda x: x[1]["SPEED"], reverse = True):
        print(dino)
