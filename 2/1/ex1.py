from dataclasses import dataclass   #to make student class
from typing import List, Dict       #to use in Student class

@dataclass

class Student:

    """A student's course registration details"""

    given_name: str

    surname: str

    registered_courses: List[str]

def load_course_registrations(filename: str) -> List[Student]:

    students = []  #list to store student objects

    with open(filename) as file:    #open input file

        for line in file:   #using a loop to create student objects and store them in a list
            row = line.strip()
            fname,lname,*courses = row.split(',')
            student = Student(fname,lname,courses)
            students.append(student)
           
    return students #return list 1(a)

x = load_course_registrations("details.txt") #calling to read the file and get list of students
print(x[0]) #checking values
print(x[1])
print(x[2])
print(x[3])
print(x[4])
