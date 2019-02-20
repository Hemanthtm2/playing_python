#!/usr/bin/python

class Engine():
      def start(self):
          pass
      def stop(self):
          pass

class ElecticEngine(Engine):
      pass

class V8Engine(Engine):
      pass


class Car():
      engine_cls=Engine
      def __init__(self):
          self.engine=self.engine_cls()
      def start(self):
          print('Starting engine {0} of the car {1}....Wroom,Wrrom'.format(self.engine.__class__.__name__,self.__class__.__name__))
          self.engine.start()
      def stop(self):
          self.engine.stop()
class RaceCar(Car):
      engine_cls=V8Engine

class CityCar(Car):
      engine_cls=ElecticEngine

class F1Car(RaceCar):
      engine_cls=V8Engine


car=Car()
racecar=RaceCar()
citycar=CityCar()
f1car=F1Car()

cars=[car,racecar,citycar,f1car]

for car in cars:
    car.start()

         
