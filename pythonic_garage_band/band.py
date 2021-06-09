class Musician:
    def __init__(self,name):
        self.name=name

        
class Guitarist(Musician):      #(self,name) joan obj in test have a name ('joan jett')
    def __str__(self):
         return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar' 







class Bassist:
    name=''

class Drummer:
    name=''


class Band:
    name=''