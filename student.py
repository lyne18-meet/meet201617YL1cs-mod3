class Student:
    def __init__ (self,name,hometown,age,hight,favorite_ice_cream_flavor):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.hight = hight
        self.favorite_ice_cream_flavor = favorite_ice_cream_flavor
    def print_summary(self):
        print('this is '+ self.name +\
              ' she lives in ' + self.hometown + \
              ' she is '+ self.age+' she is '+ self.hight + \
              ' and she likes ' + self.favorite_ice_cream_flavor +' ice cream.')


    def get_girrafe_gap(self):
        return (500-int(self.hight))
new_student1 = Student("Nadia","Jerusalem",'15','160','vanilla')
new_student2 = Student("Noura","Ramalla",'16','170','Choclate')

new_student1.print_summary()
new_student2.print_summary()

new_student2.get_girrafe_gap()



