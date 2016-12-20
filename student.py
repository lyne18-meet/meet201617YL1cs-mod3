import time
class Student:
    def __init__ (self,name,hometown,age,hight,favorite_ice_cream_flavor,birthday_month,birthday_day):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.hight = hight
        self.favorite_ice_cream_flavor = favorite_ice_cream_flavor
        self.birthday_month=birthday_month
        self.birthday_day=birthday_day
    def print_summary(self):
        print('this is '+ self.name +\
              ' she lives in ' + self.hometown + \
              ' she is '+ self.age+' she is '+ self.hight + \
              ' and she likes ' + self.favorite_ice_cream_flavor +' ice cream.')


    def get_girrafe_gap(self):
        return (500-int(self.hight))
    def get_days_to_birthday(self):
        number_of_days=(time.mktime((time.localtime()[0],self.birthday_month,self.birthday_day,0,0,0,0,0,0))-time.time())/(60*60*24)
        if number_of_days>=0:
            return number_of_days
        else:
            return (time.mktime((time.localtime()[0]+1,self.birthday_month,self.birthday_day,0,0,0,0,0,0))-time.time())/(60*60*24)
            
    
new_student1 = Student("Nadia","Jerusalem",'15','160','vanilla',8,7)
new_student2 = Student("Theodore","NewYork",'32','177','green tee',1,17)
print (new_student1.get_days_to_birthday())
print (new_student2.get_days_to_birthday())

new_student1.print_summary()
new_student2.print_summary()

new_student2.get_girrafe_gap()



