from dataclasses import dataclass

from typing import List, Dict

@dataclass

class Student:

    """A student's course registration details"""

    given_name: str

    surname: str

    registered_courses: List[str]

def load_course_registrations(filename: str) -> List[Student]:

    students = []
    """ Returns a list of Student objects read from filename"""
    with open(filename) as f:

        for line in f:
            line = line.strip()

            fname, lname, *courses = line.split(',')

            student = Student(fname,lname,courses)
            students.append(student)

    
    return sorted(students, key = lambda s: s.surname + s.given_name)

x = load_course_registrations("details.txt") #calling to read the file and get list of students
print(x[0]) #checking values
print(x[1])
print(x[2])
print(x[3])
print(x[4])
