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

from collections import math
from collections import defaultdict

def get_speed(str_len, leg_len):
    str_len = float(str_len)
    leg_len = float(len_len)
    dino_speed = ((str_len/leg_len) - 1) * sqrt(leg_len * 9.8)
    return dino_speed

def read_csv(filename):
    csv_as_list = []
    f = open(filename, "rU")
    f_lines = f.readlines()
    for line in f_lines:
        line.strip("\n")
        new_line = line.split(",")
        csv_as_list.append(new_line)
    f.close()
    return csv_as_list

def get_bipedals_by_speed(datafiles):
    keep = defaultdict(dict)  #-> {"name": {"stride_len": float , "leg_len": float, "speed": float }}
    res = []
    for datafile in datafiles:
        dino_data = read_csv(datafile)
        name_indx = dino_data[0].getindex("NAME")
        if "STANCE" in dino_data[0]:
            stance_indx = dino_data[0].getindex("STANCE")
            for data in dino_data:
                if data[stance_indx] == "bipedal":
                    keep[data[name_indx]] = defaultdict()

    for datafile in datafiles:
        dino_data = read_csv(datafile)
        name_indx = dino_data[0].getindex("NAME")
        if len(keep) > 0 and "STRIDE_LENGTH" in dino_data[0]:
            stride_indx = dino_data[0].getindex("STRIDE_LENGTH")
            for data in dino_data:
                keep[data[name_indx]]["stride_len"] = data[stride_indx]

    for datafile in datafiles:
        dino_data = read_csv(datafile)
        name_indx = dino_data[0].getindex("NAME")
        if len(keep) > 0 and "LEG_LENGTH" in dino_data[0]:
            leg_indx = dino_data[0].getindex("LEG_LENGTH")
            for data in dino_data:
                keep[data[name_indx]]["leg_len"] = data[leg_indx]

    for name in keep:
        dino_speed = get_speed(keep[name]["stride_len"], keep[name]["leg_len"])
        keep[name]["speed"] = dino_speed

    for dino in sorted(keep.items(), key = lambda x: x[1]["speed"], reverse = True):
        print(dino[0])


dino_files = ["csv1.csv", "csv2.csv"]
get_bipedals_by_speed(dino_files)
