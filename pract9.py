class Family:
    """
    This class represents a family of an expected child.
    """
    def __init__(self, dad, mom, sib):
        self.dad = dad
        self.mom = mom
        self.sib = sib

    def __str__(self):
        return f"Father: {self.dad}, Mother: {self.mom}, Sibling: {self.sib}"

    def getFamilyInfo(self):
        return ( f"Father's name: {self.dad} \
                 Mother's name: {self.mom} \
                 Sibling's name: {self.sib}." )


class Child(Family):
    """
    This class represents the child characteristics.
    """
    def __init__(self, dad, mom, sib, baby, gender, height, weight):
        super().__init__(self, dad, mom, sib)
        self.baby = baby
        self.gender = gender
        self.height = height
        self.weight = weight

    def getBabyInfo(self):
         return( f"Hello I am baby {self.baby}. \
                I am a {self.gender}. \
                I am {self.height} feet tall. \
                I weigh {self.weight} lbs." )


Fam1 = Family("jay", "vini", "yohan")
