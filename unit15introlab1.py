#! /usr/bin/python
# Unit 15 Intro Lab 1
# File Name: unit15introlab1.py
# Programmer: Ethan Machado
# Date: July 16, 2023
#
# Problem Statement: Creating a Class (person object)
#
#
# Overall Plan:
# 1. Create a class with a person object
# 2. Create a constructor
# 3. Create an instance method
# 4. Create two person objects
# 5. Print the person objects' attributes to the screen
#
# import the necessary python libraries
# none are needed


# constructor
class Person:

  def __init__(self):
    # attributes associated with person objects
    self.name = "n/a"
    self.age = 0
    self.weight = 0.0

  # instance method
  def print_person(self):
    print(f'    Name: {self.name}')
    print(f'    Age: {self.age}')
    print(f'    Weight: {self.weight}')


if __name__ == "__main__":
  # instance of a person object
  person1 = Person()
  person1.name = "Kanye West"
  person1.age = 44
  person1.weight = 204.5
  person1.print_person()

  # instance of a person object
  person2 = Person()
  person2.name = "Kim Kardashian"
  person1.age = 45
  person2.weight = 170.3
  person2.print_person()