from dataclasses import asdict      #to use asdict
from dataclasses import dataclass   #to make student class
from typing import List, Dict       #to use in Student class
from json import dump               #to dump dictionaries to a .json file 

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
           
    return students #return list

Student_list = load_course_registrations("details.txt")     #calling to read the file and get list of students

s1 = list(map(lambda x: asdict(x), Student_list))   #mapping objects in above list to dictionaries 4(c)

with open("student_registrations.json", "w") as registrations:  #store them in a json file  4(d)
    dump(s1, registrations)
