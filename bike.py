#!/usr/bin/python 

class Bike:
    def __init__(self,color,fmaterial):
                self.color=color
                self.fmaterial=fmaterial
    def brake(self):
        print('braking')

red_bike=Bike('Red','metal')
blue_bike=Bike('Blue','iron')
print (red_bike.color)
print(red_bike.fmaterial)
print(blue_bike.color)
print(blue_bike.fmaterial)

red_bike.brake()
blue_bike.brake()
