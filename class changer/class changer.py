import time


class Person:
    def __init__(self, name, age, person_type):
        self.name = name
        self.age = age
        self.person_type = person_type
    
    def change_type(self):
        if self.person_type == 'worker':
            self.__class__ = Warrior
            self.person_type = 'warrior'
            self.__init__(self.name, self.age, self.person_type, input('what art do you know: '), 0)
        else:
            self.__class__ = Worker
            self.person_type = 'worker'
            self.__init__(self.name, self.age, self.person_type, input('what is your job: '), input('what is your talent: '))




class Worker(Person):
    def __init__(self, name, age, person_type, job, talent):
        super().__init__(name, age, person_type)
        self.job = job
        self.talent = talent
    
    def talk(self):
        print('Hello I am Worker my job is ' + self.job + ' but my talent is ' + self.talent)





class Warrior(Person):
    def __init__(self, name, age, person_type, art, level):
        super().__init__(name, age, person_type)
        self.art = art
        self.level = level

    def talk(self):
        print('Hello I am Warrior my level is ' + str(self.level) + ' and my art is ' +  self.art) 

almog = Worker('almog', 17, 'worker', 'engineer', 'buissnes')





counter = 0
while counter < 10:
    almog.talk()
    almog.change_type()
    print(almog.person_type)
    counter = counter + 1
    time.sleep(1)



