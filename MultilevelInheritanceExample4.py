class Animal:

    def eat(self):
      print 'Eating...'

class Dog(Animal):
   def bark(self):
      print 'Barking...'

class BabyDog(Dog):
    def weep(self):
        print 'Weeping...'

d=BabyDog()
d.eat()
d.bark()
d.weep()


#We can inherit a derived class from another derived class, this process is known as multilevel inheritance.