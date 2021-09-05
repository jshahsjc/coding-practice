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
from math import sqrt
from collections import defaultdict
import csv

def getSpeed(str_len, leg_len):
    return ((str_len / leg_len) - 1) * sqrt(leg_len * 9.8)

def getBipedalDino(datafile1, datafile2):
    keep = defaultdict(dict)
    res = defaultdict()
    res_list = []
    with open(datafile2) as f:
        csv_f = csv.reader(f)
        # This will create csv_f obj as list of list of strs ( 1 list per line of data )
        for data in csv_f:
            if data[2] == 'bipedal':
                keep[data[0]]['stance'] = 'bipedal'
                keep[data[0]]['str_len'] = float(data[1])
    with open(datafile1) as f:
        csv_f = csv.reader(f)
        for data in csv_f:
            if data[0] in keep:
                keep[data[0]]['leg_len'] = float(data[1])
    for k, v in keep.items():
        if 'str_len' and 'leg_len' in v:
            res[k] = getSpeed(v['str_len'], v['leg_len'])
    for name, speed in sorted(res.items(), key = lambda x: x[1], reverse = True):
        print(name)
    #    res_list.append((name, speed))
    #return res_list



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

def readCsv(csv):
    f = open(csv, "rU")
    lines = f.readlines()
    new_lines = []
    for line in lines:
        line = line.strip("\n")
        new_lines.append(line.split(","))
    f.close()
    return new_lines

#print(readCsv("csv1.csv"))

def get_dino(csv1, csv2):
    g = 9.8
    dino_data1 = defaultdict(list)
    temp = [] # list of tuples
    result = []
    read_csv2 = readCsv(csv2)
    read_csv1 = readCsv(csv1)
    print(read_csv2)
    for line in read_csv1:
        dino_data1[line[0]] = line[1:]
    print("dino_data1:", dino_data1)
    for line in read_csv2:
        dino_name = line[0]
        print("inside for" + str(line))
        print(line[-1])
        if str(line[-1]) == 'bipedal' and dino_name in dino_data1:
            print("inside if:")
            leg_len = dino_data1[dino_name][0]
            str_len = line[1]
            speed = ((float(str_len)/float(leg_len))-1) * (sqrt(float(leg_len) * g))
            temp.append((line[0], speed))

    print("temp:", temp)
    result = sorted(temp, key = lambda x: x[1], reverse = True)
    print("result:",result)
    for r in result:
        print(r[0])


get_dino("csv1.csv", "csv2.csv")
