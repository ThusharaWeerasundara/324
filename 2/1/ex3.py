from dataclasses import dataclass

from typing import List, Dict

@dataclass

class Student:

    """A student's course registration details"""

    given_name: str

    surname: str

    registered_courses: List[str]

def load_course_registrations(filename: str) -> Dict[tuple,Student]:  

    students = {}   #dictionary to store student objects

    with open(filename) as file:    #open input file

        for line in file:   #using a loop to create student objects and store them in a dictionary

            row = line.strip()
            fname,lname,*courses = row.split(',')
            student = Student(fname,lname,courses)
            students[(lname,fname)] = student #use a tuple as a key 3(a)

    
    return students #return dictionary

x = load_course_registrations("details.txt")    #creating dictionary of students
print(x[('Chandrasiri','Gayan')])   #testing
print(x[('Gunarathne','Manjula')])   #testing

