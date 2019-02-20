#!/usr/bin/python

class Engine():
      def start(Self):
          pass
      def stop(self):
          pass

class ElectricEngine(Engine):
      pass

class V8Engine(Engine):
      pass

class Car():
      engine_cls=Engine
      
      def __init__(self):
          self.engine=self.engine_cls()
    
      def start(self):
          print('Starting engine {0} for car {1}... Wroom,Wroom!'.format(self.engine.__class__.__name__,self.__class__.__name__))
          self.engine.start()

      def stop(self):
           self.engine.stop()

class Racecar(Car):
      engine_cls=V8Engine

class Citycar(Car):
      engine_cls=ElectricEngine

class F1car(Racecar):
      engine_cls=V8Engine

car=Car()
racecar=Racecar()
citycar=Citycar()
f1car=F1car()
cars=[car,racecar,citycar,f1car]

for car in cars:
    car.start()
