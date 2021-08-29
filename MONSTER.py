

class MONSTER:
    name=""
    terrain=""
    hp = 0
    ac = 0
    chalangeRating=0


    def GetChallange(self):
        return self.chalangeRating


    def MONSTER(self,name,ter,chr,hp,ac):
        self.name = name
        self.terrain = ter
        self.chalangeRating = chr
        self.hp = hp
        self.ac = ac